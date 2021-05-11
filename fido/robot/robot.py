import typing
from abc import ABC, abstractmethod
from typing import Any, Callable, List, Mapping, Type

from ..errors import NotImplementedError, RobotError

if typing.TYPE_CHECKING:
    from ..world import World
    from .component import Sensor


class Robot(ABC):
    """Represents a physical robot.

    A robot is a navigable collection of sensors modeled by a
    `fido.robot.Model`  which describes its physical appearance. Fido
    provides a collection of premade robots that can be used directly in
    a simulation.
    """

    _sensors: List["Sensor"] = []
    _closers: List[Callable[[], None]] = []

    def __init__(self, name: str, model_name: str):
        self.name = name
        self.model_name = model_name

    def add_sensor(
        self, sensor_cls: Type["Sensor"], sensor_args: Mapping[str, Any] = {}
    ) -> None:
        """Add sensor to the robot."""
        self._sensors.append(sensor_cls(self, **sensor_args))

    def prepare(self) -> None:
        """Prepare initializes all the sensors in the robot."""
        self.__init_sensors()

    def __init_sensors(self):
        for s in self._sensors:
            c = s.handle_updates(self.world.ros())
            self._closers.append(c)

    def set_world(self, world: "World") -> None:
        """Set the world to use for this robot."""
        self.world = world

    @abstractmethod
    def move(self, distance: float = 0, duration: float = 0, speed: float = 0) -> None:
        """Move the robot at a certain distance at a certain speed or for a
        certain duration.

        To move backwards, set speed to negative. If the given speed is
        larger than the maximum speed, it will be set to the maximum
        speed.
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
        """
        raise RobotError(
            "failed to call method on abstract robot"
        ) from NotImplementedError("rotate() not implemented")

    @abstractmethod
    def stop(self, forced: bool = False) -> None:
        """Stop the robot.

        This is a blocking call. It will block execution until the robot
        is gracefully stopped unless `forced` is set to `True`.
        """
        raise RobotError(
            "failed to call method on abstract robot"
        ) from NotImplementedError("stop() not implemented")
