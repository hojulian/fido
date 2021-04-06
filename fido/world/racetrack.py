from ..robot import Robot
from ..ros import LaunchFile, InstallFile
from .world import World


class RaceTrack(World):
    """Represents a RaceTrack world.

    For details about this world, see:
    https://github.com/aws-robotics/aws-robomaker-racetrack-world.
    """

    def __init__(self):
        self._install_file = InstallFile()
        self._launch_file = LaunchFile("racetrack")
        self.__include_this_world()
        super().__init__()

    def __include_this_world(self):
        self._install_file.git(
            "src/aws-robomaker-racetrack-world",
            "https://github.com/aws-robotics/aws-robomaker-racetrack-world.git",
            "master",
        )

        self._launch_file.include(
            "$(find gazebo_ros)/launch/empty_world.launch",
            {
                "world_name": "$(find aws_robomaker_racetrack_world)/world/racetrack_day.world",
                "paused": "false",
                "use_sim_time": "true",
                "gui": "true",
                "headless": "false",
                "debug": "false",
            },
        )

    def add(self, robot: Robot, x=-4.25, y=-15.0, z=0.0):
        """Add a robot to the world.

        Internally, this is converted into a gazebo_ros spawn_model call.
        """
        # Add robot dependency to install file
        robot.fill_dependency(self._install_file)

        # Add robot to launch file
        self._launch_file.param(
            f"{robot.name}_robot_description", robot.robot_description()
        )
        self._launch_file.node(
            "gazebo_ros",
            "spawn_model",
            f"spawn_{robot.model_name}",
            f"-urdf -model {robot.model_name} -x {x} -y {y} -z {z} -param {robot.name}_robot_description",
        )

    def remove(self, robot: Robot):
        """Remove a robot from the world.

        Internally, this is converted into a gazebo_ros delete_model call.
        """
        pass

    def export_files(self, path):
        self._install_file.to_file(path)
        self._launch_file.to_file(path)
