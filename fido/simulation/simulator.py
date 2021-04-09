from abc import ABC, abstractmethod

from ..errors import NotImplementedError, SimulatorError


class Simulator(ABC):
    """Represents a simulator.

    A simulator provides a ROS compatible physics engine for running a
    simulation.

    Currently, there is only one supported simulator implementation: Gazebo.
    """

    def __init__(self, gui=True):
        self._gui = gui

    @abstractmethod
    def start(self):
        """Start the simulator.

        This starts the clock of the simulator.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("start() not implemented")

    @abstractmethod
    def stop(self):
        """Pause the simulator.

        This will stop the simulation time as well.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("stop() not implemented")

    @abstractmethod
    def reset(self):
        """Reset the simulator.

        This will cause the simulator to reset itself to its original state.
        It allows the simulator to reset without doing a destroy() and start().
        This is useful in machine learning applications where each iteration
        requires a fresh state.

        The reset behavior depends on the simulator’s implementation.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("reset() not implemented")

    @abstractmethod
    def shutdown(self):
        """Exit the simulator.

        This will cause the simulator to exit. An error will be raised if the
        simulator exited with a non-zero exit code.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("shutdown() not implemented")

    @abstractmethod
    def view(self):
        """Visualize the simulator view.

        This will display the view in a `IPython.core.display.display`. This is
         compatible with Jupyter notebook.

        Currently, there is no way to adjust the view just yet.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("view() not implemented")

    @abstractmethod
    def time(self):
        """Return the simulator time."""
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("time() not implemented")
