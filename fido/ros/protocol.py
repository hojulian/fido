import typing
from abc import abstractmethod
from typing import Protocol

from .installfile import InstallFile

if typing.TYPE_CHECKING:
    from roslibpy import Ros


class RobotProtocol(Protocol):
    """RobotProtocol is implemented by a robot that is ROS compatible."""

    @abstractmethod
    def connect(self, host: str, port: int) -> None:
        """Connect to the robot via ROS bridge.

        Args:
            host (str): Name or IP address of the ROS bridge host, e.g. `127.0.0.1`.
            port (int): ROS bridge port, e.g. `9090`.
        """
        raise NotImplementedError("not implemented in robot protocol")

    @abstractmethod
    def ros_robot_description(self) -> str:
        """Return the ROS specific robot description.

        This is mainly used for building the launch file. E.g.
        `robot_description/urdf/model.urdf`.

        Returns:
            The robot_description used by the launch file.
        """
        raise NotImplementedError("not implemented in robot protocol")

    @abstractmethod
    def ros_fill_dependency(self, installfile: InstallFile) -> None:
        """Fill the needed dependencies to the given installfile.

        E.g.
        ```python
        installfile.git(
            "src/turtlebot3",
            "https://github.com/ROBOTIS-GIT/turtlebot3.git",
            "master",
        )`
        ```

        Args:
            installfile (InstallFile): InstallFile for filling dependencies.
        """
        raise NotImplementedError("not implemented in robot protocol")

    @abstractmethod
    def ros(self) -> "Ros":
        """Return internal ROS client.

        Returns:
            The ROS client.
        """
        raise NotImplementedError("not implemented in robot protocol")


class WorldProtocol(Protocol):
    """WorldProtocol is implemented by a world that is ROS compatible."""

    @abstractmethod
    def ros(self) -> "Ros":
        """Return internal ROS client.

        Returns:
            The ROS client.
        """
        raise NotImplementedError("not implemented in world protocol")


class SimulatorProtocol(Protocol):
    """SimulatorProtocol is implemented by a simulator that is ROS compatible."""

    @abstractmethod
    def ros(self) -> "Ros":
        """Return internal ROS client.

        Returns:
            The ROS client.
        """
        raise NotImplementedError("not implemented in simulator protocol")
