from abc import abstractmethod
from typing import Callable

from roslibpy import Ros, Topic

from ...errors import NotImplementedError, RobotError
from ...ros import RobotProtocol


class Sensor(object):
    robot: RobotProtocol

    def __init__(self, robot: RobotProtocol, **kwargs):
        self.robot = robot
        for k, v in kwargs.items():
            setattr(self, k, v)

    @abstractmethod
    def handle_updates(self, ros: Ros) -> Callable[[], None]:
        raise RobotError(
            "failed to call method on abstract sensor"
        ) from NotImplementedError("handle_updates() not implemented")


class Odomer(Sensor):
    def handle_updates(self, ros):
        topic = Topic(ros, "/odom", "nav_msgs/Odometry")
        topic.subscribe(self.__odom_handler)

        return lambda: topic.unsubscribe()

    def __odom_handler(self, msg):
        x = msg["pose"]["pose"]["position"]["x"]
        y = msg["pose"]["pose"]["position"]["y"]
        z = msg["pose"]["pose"]["position"]["z"]

        setattr(self.robot, "x", x)
        setattr(self.robot, "y", y)
        setattr(self.robot, "z", z)


class Lidar(Sensor):
    def handle_updates(self, ros):
        topic = Topic(ros, "/scan", "sensor_msgs/LaserScan")
        topic.subscribe(self.__scan_handler)

        return lambda: topic.unsubscribe()

    def __scan_handler(self, msg):
        ranges = msg["ranges"]

        setattr(self.robot, "ranges", ranges)
