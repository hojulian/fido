class Error(Exception):
    """A generic error that is raised when Fido execution fails.

    Whenever possible, the session will raise a more specific subclass of 
    `Error` from the `fido.errors` module.
    """

    def __init__(self, msg):
        """Creates a new `Error` indicating that an error has occurred.
        Args:
            msg (str): The message string describing the error.
        """
        self._msg = msg

    @property
    def msg(self):
        """The error message that describes the error."""
        return f"{self.__class__}: {self._msg}"


class RobotError(Error):
    """Represents a robot error raised by the underlying robot.

    This is a wrapper around any error raised by `fido.robot.Robot`.
    """

    def __init__(self, msg):
        super(RobotError, self).__init__(msg)


class SimulationError(Error):
    """Represents a simulation error by the underlying simulation framework.

    This is a wrapper around any error raised by `fido.simulation.Simulation`.
    """

    def __init__(self, msg):
        super(SimulationError, self).__init__(msg)


class SimulatorError(Error):
    """Represents a simulator error by the underlying simulator.

    This is a wrapper around any error raised by `fido.simulation.Simulator`.
    """

    def __init__(self, msg):
        super(SimulatorError, self).__init__(msg)


class ModelError(Error):
    """Represents a model error raised by the Fido's model builder.

    This is a wrapper around any error raised by `fido.robot.model.Model`.
    """

    def __init__(self, msg):
        super(ModelError, self).__init__(msg)


class WorldError(Error):
    """Represents a world error raised by the underlying world.

    This is a wrapper around any error raised by `fido.world.World`.
    """

    def __init__(self, msg):
        super(WorldError, self).__init__(msg)


class DockerError(Error):
    """Represents a docker error raised by the underlying docker client.

    This is a wrapper around any error raised by the internal docker client.
    """

    def __init__(self, msg):
        super(DockerError, self).__init__(msg)


class NotImplementedError(Error):
    """Represents an error for calling a not yet implemented method.
    """

    def __init__(self, msg):
        super(NotImplementedError, self).__init__(msg)
