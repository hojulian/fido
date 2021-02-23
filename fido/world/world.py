from ..robot import Robot


class World(object):
    """Represents a world.

    Currently this is only compatible with Gazebo.
    """

    def add(self, robot: Robot, x, y, z):
        """Add a robot to the world.

        Internally, this is converted into a gazebo_ros spawn_model
        call.
        """
        pass

    def remove(self, robot: Robot):
        """Remove a robot from the world.

        Internally, this is converted into a gazebo_ros delete_model
        call.
        """
        pass

    def gazebo_world(self, path):
        """Exports a gazebo compatible `.world` representation of the world.
        """
        pass
