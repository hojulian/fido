from ..ros import InstallFile
from .robot import Robot


class Turtlebot3(Robot):
    """Represents a Turtlebot3 Burger robot.

    For details about this robot, see:
    https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/.
    """

    def __init__(self, name):
        super().__init__(name, "turtlebot3_burger")

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
            "src/turtlebot3", "https://github.com/ROBOTIS-GIT/turtlebot3.git", "master"
        )
