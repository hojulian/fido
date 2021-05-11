import typing
from multiprocessing import Process

from docker.errors import APIError
from roslibpy import Ros

from ..core import Core
from ..errors import DockerError, SimulationError, SimulatorError
from ..ros import gather_dependencies, init_package, prepare_workspace

if typing.TYPE_CHECKING:
    from IPython.display import IFrame

    from ..world import World
    from .simulator import Simulator


class Simulation(object):
    """Represents a single simulation.

    A simulation is made out of two things: a world `fido.world.World` and a
    simulator `fido.simulation.Simulator` for running the simulation.

    Note that both the simulator and world need to be compatible.

    When a Simulation is created, it will first initialize by loading all the external
    world and robot files using rosinstall. Then, it will create a docker container with
    the files attached to the catkin workspace. The container created will be in a pause
    state. To start the container and simulation, call `start()`.
    """

    def __init__(self, simulator: "Simulator", world: "World", use_sim_time=True):
        self._simulator = simulator
        self._world = world
        self._use_sim_time = use_sim_time

        self._sim_id = Core.generate_sim_id()
        self._package_path = f".fido/sim_{self._sim_id}"
        self._package_name = "fido_simulation"
        self._vnc_port = Core.generate_port()
        self._rosbridge_port = Core.generate_port()

        # Prepare workspace and simulation package
        try:
            prepare_workspace(self._package_path)
            init_package(self._package_path, self._package_name)
            world.export_files(
                self._package_path, self._package_name, self._rosbridge_port
            )
            gather_dependencies(self._package_path)
        except (OSError) as exc:
            raise SimulationError("failed to prepare simulation package") from exc
        # Create container
        try:
            self._container_id = Core.create_container(
                self._sim_id,
                self._package_path,
                vnc_port=self._vnc_port,
                rosbridge_port=self._rosbridge_port,
            )
        except (DockerError) as exc:
            raise SimulationError("failed to create simulation container") from exc

        # Connect all involved components
        self._simulator.set_simulation(self)
        self._world.set_simulation(self)

    def start(self) -> None:
        """Start the simulation.

        Multiple simulations can be started at the same time. This is a
        blocking call, it will block until the Simulator is successfully
        started.

        Internally, this creates a new docker container containing the
        `Simulator`, `World`, and `Robot` needed for the simulation. Once the
        container is started, it will first build all the packages in the directory
        using catkin_make. Then, fido will start the simulation by launching the launch
        file on a seperate thread. Once the launch file is ready, fido will create a
        persistent connection with ROS master running in the container using rosbridge.
        """
        try:
            # Start container
            Core.start_container(self._container_id)

            # Compile all packages
            self.__catkin_make()

            # Start launch file
            self._sim_proc = Process(target=self.__start_launch_file, daemon=True)
            self._sim_proc.start()
        except DockerError as exc:
            raise DockerError("failed to start container") from exc

        # Connect to simulation
        try:
            # Start ros connection
            self.__start_ros_client()

            # Prepare robots
            self._world.prepare_robots()

            # Start ros client
            # Default timeout: 30 seconds
            self._ros.run(30)
        except (SimulatorError, Exception) as exc:
            raise SimulationError("failed to start simulation") from exc

    def __start_ros_client(self):
        host = "localhost"
        port = self._rosbridge_port
        client = Ros(host=host, port=port)
        self._ros = client

    def __catkin_make(self):
        try:
            exit_code, out = Core.container_exec(
                self._container_id,
                self.__with_bash("cd /workspace/fido_ws/ && catkin_make"),
            )
            if exit_code != 0:
                raise Exception(
                    f"exited with a non-zero exit code: {exit_code}\nout: {out}"
                )
        except (APIError, Exception) as exc:
            raise DockerError("failed to run catkin_make") from exc

    def __with_bash(self, cmd):
        ros_setup = "/opt/ros/melodic/setup.bash"
        package_setup = "/workspace/fido_ws/setup.bash"
        return f'/bin/bash -c "source {ros_setup} && source {package_setup} && {cmd}"'

    def __with_catkin_bash(self, cmd):
        ros_setup = "/opt/ros/melodic/setup.bash"
        package_setup = "/workspace/fido_ws/setup.bash"
        catkin_setup = "/workspace/fido_ws/devel/setup.bash"
        return f'/bin/bash -c "source {ros_setup} && source {package_setup} && source {catkin_setup} && {cmd}"'

    def __start_launch_file(self):
        try:
            exit_code, out = Core.container_exec(
                self._container_id,
                self.__with_catkin_bash("roslaunch fido_simulation simulation.launch"),
            )
            if exit_code != 0:
                raise Exception(
                    f"exited with a non-zero exit code: {exit_code}\nout: {out}"
                )
        except (APIError, Exception) as exc:
            raise DockerError("failed to run launch file") from exc

    def ros(self) -> Ros:
        """Returns the ros client."""
        if self._ros is None:
            self.__start_ros_client()
        return self._ros

    def stop(self) -> None:
        """Stop the simulation.

        This will pause the simulator engine. Note that this is not sufficient
        to end the simulation completely, this merely pauses the simulation.

        To end a simulation, use `Simulation.destroy()`. It is not necessary
        to call `Simulation.stop()` before `Simulation.destroy()`.
        """
        try:
            self._simulator.stop()
        except SimulatorError as exc:
            raise SimulationError("failed to stop simulation") from exc

    def reset(self) -> None:
        """Reset the simulation.

        This will cause the simulation to reset itself to its original state.
        It allows the simulation to reset without doing `Simulation.destroy()`
        and `Simulation.start()`.

        This is useful in machine learning applications where each iteration
        requires a fresh state.

        The exact reset behavior depends on the underlying simulator
        implementation.
        """
        try:
            self._simulator.reset()
        except SimulatorError as exc:
            raise SimulationError("failed to reset simulation") from exc

    def destroy(self) -> None:
        """Destroy the simulation.

        This will forcefully destroy the container containing the simulation.

        Once the simulation is destroyed, it can never be started again.
        """
        self._sim_proc.terminate()

        try:
            Core.remove_container(self._container_id)
        except APIError as exc:
            raise DockerError("failed to destroy container running simulation") from exc

    def view(self) -> "IFrame":
        """Visualize the simulation.

        This will display the simulation in a `IPython.core.display.display()`.
        This is compatible with Jupyter notebook.
        """
        try:
            return self._simulator.view()
        except SimulatorError as exc:
            raise SimulationError("failed to view simulation") from exc

    @property
    def container_id(self) -> str:
        """Return the docker container ID of this simulation.

        This is used by simulator to execute command on the undelying docker container.

        Although not recommended, this container ID can be used with docker-cli to
        access and manage the simulation container.
        """
        return self._container_id

    @property
    def vnc_port(self) -> str:
        """Return vnc port.

        This is used by simulator for accessing the VNC viewport.
        """
        return str(self._vnc_port)

    def time(self) -> float:
        """Return the simulation time.

        This can be either simulator time or wall time depending on the
        `use_sim_time` flag on creation.
        """
        try:
            return self._simulator.time()
        except SimulatorError as exc:
            raise SimulationError("failed to get simulation time") from exc
