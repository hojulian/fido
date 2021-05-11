import json
import math
from dataclasses import dataclass
from typing import List, Protocol

import numpy as np
from roslibpy import Message


class DType(Protocol):
    """Represents the type of the element used by sensors and components.

    It is implemented as a wrapper around common ROS messages.
    """

    def ros_msg(self) -> Message:
        return Message({})

    def ros_type(self):
        return "std_msgs/Empty"

    def str(self) -> str:
        return json.dumps(self.ros_msg().data)


class Odom(DType):
    """Represents a odometry state.

    This is equivalent to ROS's nav_msgs/Odometry.
    """

    x: float
    y: float
    z: float

    # Quaternion
    _qx: float
    _qy: float
    _qz: float
    _qw: float

    # Euler
    ro: float
    pi: float
    ya: float

    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        qx: float = 0,
        qy: float = 0,
        qz: float = 0,
        qw: float = 0,
    ):
        self.x = x
        self.y = y
        self.z = z
        self._qx = qx
        self._qy = qy
        self._qz = qz
        self._qw = qw
        self.ro, self.pi, self.ya = self.__euler_from_quaternion()

    def __euler_from_quaternion(self):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        x, y, z, w = self._qx, self._qy, self._qz, self._qw

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)

        return roll_x, pitch_y, yaw_z

    def ros_msg(self):
        msg = {
            "pose": {
                "pose": {
                    "position": {
                        "x": self.x,
                        "y": self.y,
                        "z": self.z,
                    },
                    "orientation": {
                        "x": self._qx,
                        "y": self._qy,
                        "z": self._qz,
                        "w": self._qw,
                    },
                },
                "covariance": [],
            }
        }
        return Message(msg)

    def ros_type(self):
        return "nav_msgs/Odometry"


@dataclass(repr=True)
class Twist(DType):
    """Represents a twist message.

    This is equivalent to ROS's geometry_msgs/Twist.
    """

    x: float = 0
    y: float = 0
    z: float = 0
    xx: float = 0
    yy: float = 0
    zz: float = 0

    def ros_msg(self):
        msg = {
            "linear": {
                "x": self.x,
                "y": self.y,
                "z": self.z,
            },
            "angular": {
                "x": self.xx,
                "y": self.yy,
                "z": self.zz,
            },
        }
        return Message(msg)

    def ros_type(self):
        return "geometry_msgs/Twist"


@dataclass(frozen=True, repr=True)
class LaserScan(DType):
    """Represents a laser scan in 360 degrees.

    This is equivalent to ROS's sensor_msgs/LaserScan.
    """

    range_min: float
    range_max: float
    ranges: List[float]
    intensities: List[float]

    def ros_msg(self):
        msg = {
            "range_min": self.range_min,
            "range_max": self.range_max,
            "ranges": self.ranges,
            "intensities": self.intensities,
        }
        return Message(msg)

    def ros_type(self):
        return "sensor_msgs/LaserScan"


@dataclass(frozen=True, repr=True)
class Image(DType):
    """Represents an image.

    This is equivalent to ROS's sensor_msgs/Image.
    """

    height: int
    width: int
    data: np.ndarray

    def ros_msg(self):
        msg = {
            "height": self.height,
            "width": self.width,
            "data": self.data,
        }
        return Message(msg)

    def ros_type(self):
        return "sensor_msgs/Image"
