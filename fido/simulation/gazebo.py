import typing
from multiprocessing import Process
from urllib.parse import urlencode, urlunparse

import roslibpy
from docker.errors import APIError
from IPython.display import IFrame

from ..core import Core
from ..errors import DockerError, SimulatorError
from .simulator import Simulator

if typing.TYPE_CHECKING:
    from roslibpy import Ros


class Gazebo(Simulator):
    """Represents a Gazebo simulator."""

    _started_client: bool = False

    def __init__(self, gui: bool = True):
        super().__init__(gui)

    def start(self) -> None:
        """Start the simulator.

        This starts the clock of the simulator.
        """
        try:
            self.__unpause_physics()
        except Exception as exc:
            raise SimulatorError("unable to start gazebo simulator") from exc

    def stop(self) -> None:
        """Pause the simulator.

        This will stop the simulation time as well.
        """
        try:
            self.__pause_physics()
        except Exception as exc:
            raise SimulatorError("unable to stop gazebo simulator") from exc

    def reset(self) -> None:
        """Reset the simulator.

        This will cause the simulator to reset itself to its original state.
        It allows the simulator to reset without doing a `destroy()` and `start()`.
        This is useful in machine learning applications where each iteration
        requires a fresh state.

        In gazebo, reset will restart the entire simulation including the time.
        """
        try:
            self.__reset_simulation()
        except Exception as exc:
            raise SimulatorError("unable to start gazebo simulator") from exc

    def view(self) -> IFrame:
        """Visualize the simulator view.

        This will start a gazebo GUI using gzclient and display on the noVNC page. Then
        the page is displayed as an IFrame using `IPython.core.display.display`. This is
        compatible with Jupyter notebook.

        Currently, there is no way to adjust the view just yet.

        Returns:
            Gazebo GUI in an IFrame.
        """
        if not self._started_client:
            try:
                self._client_proc = Process(target=self.__start_gzclient, daemon=True)
                self._client_proc.start()
                self._started_client = True
            except DockerError as exc:
                raise SimulatorError("failed to start client") from exc

        host = "localhost"
        port = self._simulation.vnc_port
        query = urlencode(
            {
                "path": "vnc",
                "autoconnect": "true",
                "resize": "scale",
                "reconnect": "true",
                "show_dot": "true",
                "bell": "false",
                "view_only": "false",
            }
        )
        src = urlunparse(
            (
                "http",
                f"{host}:{port}",
                "/vnc.html",
                None,
                query,
                None,
            )
        )
        return IFrame(src, "100%", "800px")

    def __start_gzclient(self) -> None:
        try:
            exit_code, out = Core.container_exec(
                self._simulation.container_id,
                "gzclient",
                env={
                    "DISPLAY": ":99",
                },
            )
            if exit_code != 0:
                raise Exception(
                    f"exited with a non-zero exit code: {exit_code}\nout: {out}"
                )
        except (APIError, Exception) as exc:
            raise DockerError("failed to start gzclient") from exc

    def time(self) -> float:
        """Return the simulator time.

        Returns:
            The simulator time.
        """
        return self._time

    def ros(self) -> "Ros":
        """Return internal ROS client.

        Returns:
            The ROS client.
        """
        return self._simulation.ros()

    def __pause_physics(self) -> None:
        srv = roslibpy.Service(self.ros(), "/gazebo/pause_physics", "std_srvs/Empty")
        req = roslibpy.ServiceRequest()
        srv.call(req)

    def __unpause_physics(self) -> None:
        srv = roslibpy.Service(self.ros(), "/gazebo/unpause_physics", "std_srvs/Empty")
        req = roslibpy.ServiceRequest()
        srv.call(req)

    def __reset_simulation(self) -> None:
        srv = roslibpy.Service(self.ros(), "/gazebo/reset_simulation", "std_srvs/Empty")
        req = roslibpy.ServiceRequest()
        srv.call(req)
