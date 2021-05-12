import time
import typing

import numpy as np
from roslibpy import Topic

from ..dtypes import Twist
from .component import Lidar, Odomer
from .robot import Robot

if typing.TYPE_CHECKING:
    from ..ros import InstallFile


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
        """Move the robot at a certain distance at a certain speed or for a
        certain duration.

        To move backwards, set speed to negative. If the given speed is
        larger than the maximum speed, it will be set to the maximum
        speed.

        Args:
            distance (float): Distance to travel.
            duration (float): Time duration to travel for (in seconds).
            speed (float): Travel speed.
        """
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
        """Rotate the robot at a certain angle at a certain speed or for a
        certain duration.

        To rotate clockwise, set the speed to positive. To rotate in
        anti-clockwise, set the speed to negative. If the given speed is
        larger  than the maximum speed, it will be set to the maximum
        speed.

        Args:
            angle (float): Angle to rotate (in degrees).
            duration (float): Time duration to rotate for (in seconds).
            speed (float): Rotation speed (radian per seconds).
        """
        # Frequency in Hertz (hz)
        freq = 10

        msg = Twist()
        t = Topic(self.ros(), "/cmd_vel", msg.ros_type())

        # Rotate at $speed for $angle
        if speed > 0 and angle != 0:
            rad = np.deg2rad(angle)
            duration = abs(rad) / speed

        # Rotate for $duration to $angle
        if duration > 0 and angle != 0:
            rad = np.deg2rad(angle)
            speed = rad / duration

        # Rotate for $duration at $speed
        if duration > 0 and speed != 0:
            msg.zz = speed

            end_time = time.time() + duration
            while time.time() <= end_time:
                t.publish(msg.ros_msg())
                time.sleep(1 / freq)

        self.stop()

    def stop(self, forced: bool = False) -> None:
        """Stop the robot.

        This is a blocking call. It will block execution until the robot
        is gracefully stopped unless `forced` is set to `True`.

        Args:
            forced (bool): Forcefully stop the robot or not.
        """
        msg = Twist()
        t = Topic(self.ros(), "/cmd_vel", msg.ros_type())
        t.publish(msg.ros_msg())

    def ros_robot_description(self) -> str:
        """Return the ROS specific robot description.

        This is mainly used for building the launch file. E.g.
        `robot_description/urdf/model.urdf`.

        Returns:
            The robot_description used by the launch file.
        """
        urdf_path = f"$(find turtlebot3_description)/urdf/{self.model_name}.urdf.xacro"
        return f"$(find xacro)/xacro --inorder {urdf_path}"

    def ros_fill_dependency(self, installfile: "InstallFile") -> None:
        """Fill the needed dependencies to the given installfile.

        Args:
            installfile (InstallFile): InstallFile for filling dependencies.
        """
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
