from roslibpy import Topic

from ..dtypes import Twist
from ..ros import InstallFile
from .component import Lidar, Odomer
from .robot import Robot


class Turtlebot3(Robot):
    """Represents a Turtlebot3 Burger robot.

    For details about this robot, see:
    https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/.
    """

    _max_speed: float
    _min_speed: float

    def __init__(self, name):
        sensors = [Lidar(), Odomer()]
        super(Turtlebot3, self).__init__(name, "turtlebot3_burger", sensors=sensors)

    def move(self, distance, duration, speed):
        pass

    def rotate(self, angle, duration, speed):
        pass

    def stop(self, forced=False):
        pass

    def ros_robot_description(self):
        urdf_path = f"$(find turtlebot3_description)/urdf/{self.model_name}.urdf.xacro"
        return f"$(find xacro)/xacro --inorder {urdf_path}"

    def ros_fill_dependency(self, installfile: InstallFile):
        installfile.git(
            "src/turtlebot3",
            "https://github.com/ROBOTIS-GIT/turtlebot3.git",
            "master",
        )
        installfile.git(
            "src/turtlebot3_simulations",
            "https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git",
            "master",
        )
        installfile.git(
            "src/turtlebot3_msgs",
            "https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git",
            "master",
        )
