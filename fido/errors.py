class Error(Exception):
    """A generic error that is raised when Fido execution fails.

    Whenever possible, the session will raise a more specific subclass of
    `Error` from the `fido.errors` module.
    """

    def __init__(self, msg: str):
        """Creates a new `Error` indicating that an error has occurred.
        Args:
            msg (str): The message string describing the error.
        """
        self._msg = msg

    @property
    def msg(self) -> str:
        """The error message that describes the error."""
        return f"{self.__class__}: {self._msg}"


class RobotError(Error):
    """Represents a robot error raised by the underlying robot.

    This is a wrapper around any error raised by `fido.robot.Robot`.
    """

    def __init__(self, msg: str):
        super(RobotError, self).__init__(msg)


class SimulationError(Error):
    """Represents a simulation error by the underlying simulation framework.

    This is a wrapper around any error raised by `fido.simulation.Simulation`.
    """

    def __init__(self, msg: str):
        super(SimulationError, self).__init__(msg)


class SimulatorError(Error):
    """Represents a simulator error by the underlying simulator.

    This is a wrapper around any error raised by `fido.simulation.Simulator`.
    """

    def __init__(self, msg: str):
        super(SimulatorError, self).__init__(msg)


class WorldError(Error):
    """Represents a world error raised by the underlying world.

    This is a wrapper around any error raised by `fido.world.World`.
    """

    def __init__(self, msg: str):
        super(WorldError, self).__init__(msg)


class DockerError(Error):
    """Represents a docker error raised by the underlying docker client.

    This is a wrapper around any error raised by the internal docker client.
    """

    def __init__(self, msg: str):
        super(DockerError, self).__init__(msg)


class DTypeError(Error):
    """Represents an error for dType."""

    def __init__(self, msg: str):
        super(DTypeError, self).__init__(msg)
