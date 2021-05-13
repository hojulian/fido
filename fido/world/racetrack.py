import typing

from .world import World

if typing.TYPE_CHECKING:
    from ..robot import Robot


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
                "world_name": "$(find aws_robomaker_racetrack_world)/worlds/racetrack_day.world",  # noqa: E501
                "paused": "false",
                "use_sim_time": "true",
                "gui": "false",
                "headless": "false",
                "debug": "false",
            },
        )

    def add(
        self, robot: "Robot", x: float = -4.25, y: float = -15.0, z: float = 0.0
    ) -> None:
        """Add a robot to the world.

        Internally, this will create the corresponding launch file instructions for
        starting the given robot. The robot dependencies are added to the `.rosinstall`
        file.

        Once the files are added, the world is added to the robot as a parent.

        Args:
            robot (Robot): Robot to be added.
            x (float): X position in the world.
            y (float): Y position in the world.
            z (float): Z position in the world.
        """
        super().add(robot, x, y, z)

    def remove(self, robot: "Robot") -> None:
        """Remove a robot from the world.

        Internally, this is converted into a gazebo_ros delete_model
        call.

        Args:
            robot (Robot): Robot to be removed.
        """
        super().remove(robot)

    def export_files(self, path: str, package: str, rosbridge_port: int) -> None:
        """Export files to a given file.

        Internally, `.rosinstall` file is exported to the root of the directory.
        The launch file is exported to $PATH/src/$PACKAGE/launch.

        Args:
            path (str): Path to export files.
            package (str): Name of simulation package. Name should only contains
                alphanumeric characters and hypens. Normally named "fido-simulation".
            rosbridge_port (int): Port number of rosbridge.
        """
        super().export_files(path, package, rosbridge_port)
