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

    def ros_urdf(self, path):
        pass

    def robot_description(self):
        return f"$(find xacro)/xacro --inorder $(find turtlebot3_description)/urdf/{self.model_name}.urdf.xacro"
