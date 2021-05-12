import time
import typing
from abc import ABC, abstractmethod

from ..errors import NotImplementedError, SimulatorError
from ..ros import SimulatorProtocol

if typing.TYPE_CHECKING:
    from IPython.display import IFrame

    from .simulation import Simulation


class Simulator(ABC, SimulatorProtocol):
    """Represents a simulator.

    A simulator provides a ROS compatible physics engine for running a
    simulation.

    Currently, there is only one supported simulator implementation: Gazebo.
    """

    _simulation: "Simulation"

    def __init__(self, gui: bool = True):
        self._gui = gui
        self._time = time.time()

    def set_simulation(self, simulation: "Simulation") -> None:
        """Set the parent simulation.

        Args:
            simulation (Simulation): Parent simulation.
        """
        self._simulation = simulation

    @abstractmethod
    def start(self) -> None:
        """Start the simulator.

        This starts the clock of the simulator.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("start() not implemented")

    @abstractmethod
    def stop(self) -> None:
        """Pause the simulator.

        This will stop the simulation time as well.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("stop() not implemented")

    @abstractmethod
    def reset(self) -> None:
        """Reset the simulator.

        This will cause the simulator to reset itself to its original state.
        It allows the simulator to reset without doing a `destroy()` and `start()`.
        This is useful in machine learning applications where each iteration
        requires a fresh state.

        The reset behavior depends on the simulator’s implementation.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("reset() not implemented")

    @abstractmethod
    def view(self) -> "IFrame":
        """Visualize the simulator view.

        This will display the view in a `IPython.core.display.display`. This is
        compatible with Jupyter notebook.

        Currently, there is no way to adjust the view just yet.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("view() not implemented")

    @abstractmethod
    def time(self) -> float:
        """Return the simulator time.

        Returns:
            The simulator time.
        """
        raise SimulatorError(
            "failed to call method on abstract simulator"
        ) from NotImplementedError("time() not implemented")
