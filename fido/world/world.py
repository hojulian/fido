from abc import ABC, abstractmethod
from future.utils import raise_from

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
        raise_from(
            WorldError("failed to call method on abstract world"),
            NotImplementedError("add() not implemented"),
        )

    @abstractmethod
    def remove(self, robot: Robot):
        """Remove a robot from the world.

        Internally, this is converted into a gazebo_ros delete_model
        call.
        """
        raise_from(
            WorldError("failed to call method on abstract world"),
            NotImplementedError("remove() not implemented"),
        )

    @abstractmethod
    def gazebo_world(self, path):
        """Exports a gazebo compatible `.world` representation of the world."""
        raise_from(
            WorldError("failed to call method on abstract world"),
            NotImplementedError("gazebo_world() not implemented"),
        )
