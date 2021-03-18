from abc import ABC, abstractmethod

from ..robot import Robot
from ..errors import WorldError, NotImplementedError


class World(ABC):
    """Represents a world.

    Currently this is only compatible with Gazebo.
    """

    @abstractmethod
    def add(self, robot: Robot, x, y, z):
        """Add a robot to the world.

        Internally, this is converted into a gazebo_ros spawn_model
        call.
        """
        raise WorldError(
            "failed to call method on abstract world"
        ) from NotImplementedError("add() not implemented")

    @abstractmethod
    def remove(self, robot: Robot):
        """Remove a robot from the world.

        Internally, this is converted into a gazebo_ros delete_model
        call.
        """
        raise WorldError(
            "failed to call method on abstract world"
        ) from NotImplementedError("remove() not implemented")

    @abstractmethod
    def launch_file(self):
        """Exports a ROS compatible `.launch` with all included robot in a given world."""
        raise WorldError(
            "failed to call method on abstract world"
        ) from NotImplementedError("launch_file() not implemented")
