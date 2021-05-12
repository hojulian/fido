import typing
from abc import ABC, abstractmethod
from typing import Any, Callable, List, Mapping, Type

from roslibpy import Ros

from ..errors import NotImplementedError, RobotError
from ..ros import RobotProtocol

if typing.TYPE_CHECKING:
    from ..ros import InstallFile
    from ..world import World
    from .component import Sensor


class Robot(ABC, RobotProtocol):
    """Represents a physical or simulated robot."""

    _ros: Ros
    _connected: bool = False

    _sensors: List["Sensor"] = []
    _closers: List[Callable[[], None]] = []

    def __init__(self, name: str, model_name: str, physical: bool = False):
        self.name = name
        self.model_name = model_name
        self.physical = physical

    def add_sensor(
        self, sensor_cls: Type["Sensor"], sensor_args: Mapping[str, Any] = {}
    ) -> None:
        """Add sensor to the robot.

        Args:
            sensor_cls (Type[Sensor]): Sensor class.
            sensor_args (dict): Arguments mapping for initializing sensor.
        """
        self._sensors.append(sensor_cls(self, **sensor_args))

    def prepare(self) -> None:
        """Prepare initializes all the sensors in the robot."""
        self.__init_sensors()

    def __init_sensors(self):
        for s in self._sensors:
            c = s.handle_updates(self.ros())
            self._closers.append(c)

    def connect(self, host: str, port: int) -> None:
        """Connect to the robot via ROS bridge.

        Args:
            host (str): Name or IP address of the ROS bridge host, e.g. `127.0.0.1`.
            port (int): ROS bridge port, e.g. `9090`.
        """
        ros = Ros(host, port)
        ros.run()
        self._ros = ros

        def _set_connecting_flag(*args):
            self._connected = True

        self._ros.on_ready(_set_connecting_flag)

    def ros(self) -> Ros:
        """Return internal ROS client.

        Returns:
            The ROS client.
        """
        if not self._connected:
            if self.physical:
                raise RobotError("ROS is not connected, please call connect() first")
            else:
                self._ros = self.world.ros()
                self._connected = True

        return self._ros

    def set_world(self, world: "World") -> None:
        """Set the world to use for this robot.

        Args:
            world (World): Parent world.
        """
        self.world = world

    @abstractmethod
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
        raise RobotError(
            "failed to call method on abstract robot"
        ) from NotImplementedError("move() not implemented")

    @abstractmethod
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
        raise RobotError(
            "failed to call method on abstract robot"
        ) from NotImplementedError("rotate() not implemented")

    @abstractmethod
    def stop(self, forced: bool = False) -> None:
        """Stop the robot.

        This is a blocking call. It will block execution until the robot
        is gracefully stopped unless `forced` is set to `True`.

        Args:
            forced (bool): Forcefully stop the robot or not.
        """
        raise RobotError(
            "failed to call method on abstract robot"
        ) from NotImplementedError("stop() not implemented")

    @abstractmethod
    def ros_robot_description(self) -> str:
        """Return the ROS specific robot description.

        This is mainly used for building the launch file. E.g.
        `robot_description/urdf/model.urdf`.

        Returns:
            The robot_description used by the launch file.
        """
        raise NotImplementedError("not implemented in robot protocol")

    @abstractmethod
    def ros_fill_dependency(self, installfile: "InstallFile") -> None:
        """Fill the needed dependencies to the given installfile.

        E.g. `installfile.git(
                "src/turtlebot3",
                "https://github.com/ROBOTIS-GIT/turtlebot3.git",
                "master",
            )`

        Args:
            installfile (InstallFile): InstallFile for filling dependencies.
        """
        raise NotImplementedError("not implemented in robot protocol")
