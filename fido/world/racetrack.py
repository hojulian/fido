from .world import World


class RaceTrack(World):
    """Represent a RaceTrack world.

    For details about this world, see:
    https://github.com/aws-robotics/aws-robomaker-racetrack-world.
    """

    def __init__(self):
        super(RaceTrack, self).__init__()
        self.__include_this_world()

    def __include_this_world(self):
        self._install_file.git(
            "src/aws-robomaker-racetrack-world",
            "https://github.com/aws-robotics/aws-robomaker-racetrack-world.git",
            "master",
        )

        self._launch_file.include(
            "$(find gazebo_ros)/launch/empty_world.launch",
            {
                "world_name": "$(find aws_robomaker_racetrack_world)/worlds/racetrack_day.world",
                "paused": "false",
                "use_sim_time": "true",
                "gui": "false",
                "headless": "false",
                "debug": "false",
            },
        )

    def add(self, robot, x=-4.25, y=-15.0, z=0.0):
        """Add a robot to the world.

        Internally, this is converted into a gazebo_ros spawn_model call.
        """
        super().add(robot, x, y, z)

    def remove(self, robot):
        """Remove a robot from the world.

        Internally, this is converted into a gazebo_ros delete_model call.
        """
        super().remove(robot)

    def export_files(self, path, package, rosbridge_port):
        """Export files to a given file.

        Internally, .rosinstall file is exported to the root of the directory.
        The launch file is exported to $PATH/src/$PACKAGE/launch.
        """
        super().export_files(path, package, rosbridge_port)
