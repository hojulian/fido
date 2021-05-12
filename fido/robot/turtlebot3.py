import time

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

    def __init__(self, name: str, physical: bool = False):
        super(Turtlebot3, self).__init__(name, "turtlebot3_burger", physical)

        self.add_sensor(Lidar)
        self.add_sensor(Odomer)

    def move(self, distance: float = 0, duration: float = 0, speed: float = 0) -> None:
        # Frequency in Hertz (hz)
        freq = 10

        msg = Twist()
        t = Topic(self.ros(), "/cmd_vel", msg.ros_type())

        # Move at $speed for $distance
        if speed > 0 and distance != 0:
            duration = distance / speed

        # Move for $duration to $distance
        if duration > 0 and distance != 0:
            speed = distance / duration

        # Move for $duration at $speed
        if duration > 0 and speed != 0:
            msg.x = speed

            end_time = time.time() + duration
            while time.time() <= end_time:
                t.publish(msg.ros_msg())
                time.sleep(1 / freq)

        self.stop()

    def rotate(self, angle: float = 0, duration: float = 0, speed: float = 0) -> None:
        return super().rotate(angle, duration, speed)

    def stop(self, forced: bool = False):
        msg = Twist()
        t = Topic(self.ros(), "/cmd_vel", msg.ros_type())
        t.publish(msg.ros_msg())

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
