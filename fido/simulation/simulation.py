import os

from docker.errors import APIError

from ..core import Core
from ..errors import DockerError, SimulationError, SimulatorError
from ..ros import gather_dependencies, init_package, prepare_workspace
from ..world import World
from .simulator import Simulator


class Simulation(object):
    """Represents a single simulation.

    A simulation is made out of two things: a world `fido.world.World` and a
    simulator `fido.simulation.Simulator` for running the simulation.

    Note that both the simulator and world need to be compatible.
    """

    def __init__(self, simulator: Simulator, world: World, use_sim_time=True):
        self._simulator = simulator
        self._world = world
        self._use_sim_time = use_sim_time
        self._sim_id = Core.generate_sim_id()
        self._package_path = f"./fido/sim_{self._sim_id}"
        self._package_name = "simulation"

        # Prepare workspace and simulation package
        try:
            prepare_workspace(self._package_path)
            init_package(self._package_name, self._package_path)
            world.export_files(self._package_path, self._package_name)
            gather_dependencies(self._package_path)
        except (OSError) as exc:
            raise SimulationError("failed to prepare simulation package") from exc
        # Create container
        try:
            self._vnc_port = Core.generate_port()
            self._rosbridge_port = Core.generate_port()
            self._container = Core.create_container(
                self._sim_id,
                self._package_path,
                vnc_port=self._vnc_port,
                rosbridge_port=self._rosbridge_port,
            )
        except (DockerError) as exc:
            raise SimulationError("failed to create simulation container") from exc

    def start(self):
        """Start the simulation.

        Multiple simulations can be started at the same time. This is a
        blocking call, it will block until the Simulator is successfully
        started.

        Internally, this creates a new docker container containing the
        `Simulator`, `World`, and `Robot` needed for the simulation. Once the
        container is started, fido will create a persistent connection with
        the ROS master running in the container.
        """
        try:
            self._container.start(detach=True)
        except APIError as exc:
            raise DockerError("failed to start container") from exc

        try:
            self.__start_rosbridge()
        except DockerError as exc:
            raise DockerError("failed to start rosbridge") from exc

        try:
            self._simulator.start()
        except SimulatorError as exc:
            raise SimulationError("failed to start simulation") from exc

    def __start_rosbridge(self):
        def with_bash(cmd):
            return f'/bin/bash -c "source /opt/ros/melodic/setup.bash && {cmd}"'

        try:
            exit_code, _ = self._container.exec_run(
                with_bash("roslaunch rosbridge_server rosbridge_websocket.launch"),
                detach=True,
                workdir="/fido_ws",
            )
            if exit_code != 0:
                raise Exception(f"exited with a non-zero exit code: {exit_code}")
        except (APIError, Exception) as exc:
            raise DockerError("failed to launch rosbridge_server") from exc

        try:
            exit_code, _ = self._container.exec_run(
                with_bash("rosrun tf2_web_republisher tf2_web_republisher"),
                detach=True,
                workdir="/fido_ws",
            )
            if exit_code != 0:
                raise Exception(f"exited with a non-zero exit code: {exit_code}")
        except (APIError, Exception) as exc:
            raise DockerError("failed to run tf2_web_republisher") from exc

    def stop(self):
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

    def reset(self):
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

    def destroy(self):
        """Destroy the simulation.

        This will forcefully destroy the container containing the simulation.

        Once the simulation is destroyed, it can never be started again.
        """
        try:
            self._container.remove(force=True)
        except APIError as exc:
            raise DockerError("failed to destroy container running simulation") from exc

    def view(self):
        """Visualize the simulation.

        This will display the simulation in a `IPython.core.display.display()`.
        This is compatible with Jupyter notebook.
        """
        try:
            self._simulator.view()
        except SimulatorError as exc:
            raise SimulationError("failed to view simulation") from exc

    def time(self):
        """Return the simulation time.

        This can be either simulator time or wall time depending on the
        `use_sim_time` flag on creation.
        """
        try:
            return self._simulator.time()
        except SimulatorError as exc:
            raise SimulationError("failed to get simulation time") from exc
