from abc import ABC, abstractmethod

from ..errors import NotImplementedError, WorldError
from ..robot import Robot


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
    def export_files(self, path, package):
        """Export all files of the World to the given path.

        Currently, it exports ROS compatible `.rosinstall` and launch file.
        """
        raise WorldError(
            "failed to call method on abstract world"
        ) from NotImplementedError("export_files() not implemented")
