from ..errors import NotImplementedError


class Robot(object):
    """Represents a physical robot.

    A robot is a navigable collection of sensors modeled by a
    `fido.robot.Model`  which describes its physical appearance. Fido
    provides a collection of premade robots that can be used directly in
    a simulation.
    """

    def __init__(self, name):
        self._name = name
        super().__init__()
        super().__init__()

    def move(self, distance, duration, speed):
        """Move the robot at a certain distance at a certain speed or for a
        certain duration.

        To move backwards, set speed to negative. If the given speed is
        larger than the maximum speed, it will be set to the maximum
        speed.
        """
        raise NotImplementedError("move() is not implemented")

    def rotate(self, angle, duration, speed):
        """Rotate the robot at a certain angle at a certain speed or for a
        certain duration.

        To rotate clockwise, set the speed to positive. To rotate in
        anti-clockwise, set the speed to negative. If the given speed is
        larger  than the maximum speed, it will be set to the maximum
        speed.
        """
        raise NotImplementedError("rotate() is not implemented")

    def stop(self, forced=False):
        """Stop the robot.

        This is a blocking call. It will block execution until the robot
        is gracefully stopped unless `forced` is set to `True`.
        """
        raise NotImplementedError("stop() is not implemented")

    def ros_urdf(self, path):
        """Exports a ROS compatible URDF representation of the robot.

        Internally, this is a wrapper around the internal
        `fido.robot.Model.ros_urdf()` method.
        """
        raise NotImplementedError("ros_urdf() is not implemented")