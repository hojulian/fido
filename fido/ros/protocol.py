from abc import abstractmethod
from typing import Protocol

from roslibpy import Ros

from ..errors import NotImplementedError
from .installfile import InstallFile


class RobotProtocol(Protocol):
    """RobotProtocol is implemented by a robot that is ROS compatible."""

    @abstractmethod
    def ros_robot_description(self) -> str:
        """Return the ROS specific robot description.

        This is mainly used for building the launch file.
        """
        raise NotImplementedError("not implemented in robot protocol")

    @abstractmethod
    def ros_fill_dependency(self, installfile: InstallFile) -> None:
        """Fill the needed dependency to the given installfile."""
        raise NotImplementedError("not implemented in robot protocol")

    @abstractmethod
    def ros(self) -> Ros:
        """Return internal ROS client."""
        raise NotImplementedError("not implemented in robot protocol")


class WorldProtocol(Protocol):
    """WorldProtocol is implemented by a world that is ROS compatible."""

    @abstractmethod
    def ros(self) -> Ros:
        """Return internal ROS client."""
        raise NotImplementedError("not implemented in world protocol")


class SimulatorProtocol(Protocol):
    """SimulatorProtocol is implemented by a simulator that is ROS compatible."""

    @abstractmethod
    def ros(self) -> Ros:
        """Return internal ROS client."""
        raise NotImplementedError("not implemented in simulator protocol")
