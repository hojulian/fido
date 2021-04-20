from abc import ABC, abstractmethod

from roslibpy import Ros, Topic

from ...errors import NotImplementedError, RobotError
from ..robot import Robot


class Sensor(ABC):
    @abstractmethod
    def handle_updates(self, robot: Robot, ros: Ros):
        raise RobotError(
            "failed to call method on abstract sensor"
        ) from NotImplementedError("handle_updates() not implemented")


class Odomer(Sensor):
    def handle_updates(self, robot: Robot, ros: Ros):
        self._robot = robot
        self._ros = ros

        topic = Topic(self._ros, "/odom", "nav_msgs/Odometry")
        topic.subscribe(self.__odom_handler)

        return lambda: topic.unsubscribe()

    def __odom_handler(self, msg):
        x = msg["pose"]["pose"]["position"]["x"]
        y = msg["pose"]["pose"]["position"]["y"]
        z = msg["pose"]["pose"]["position"]["z"]

        setattr(self._robot, "x", x)
        setattr(self._robot, "y", y)
        setattr(self._robot, "z", z)


class Lidar(Sensor):
    def handle_updates(self, robot: Robot, ros: Ros):
        self._robot = robot
        self._ros = ros

        topic = Topic(self._ros, "/scan", "sensor_msgs/LaserScan")
        topic.subscribe(self.__scan_handler)

        return lambda: topic.unsubscribe()

    def __scan_handler(self, msg):
        ranges = msg["ranges"]

        setattr(self._robot, "ranges", ranges)
