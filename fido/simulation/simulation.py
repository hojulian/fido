from future.utils import raise_from

from .simulator import Simulator
from ..errors import SimulatorError, SimulationError


class Simulation(object):
    """Represents a single simulation.
    
    A simulation is made out of two things: a world (`fido.world.World` and a 
    simulator `fido.simulation.Simulator` for running the simulation.
    
    Note that both the simulator and world need to be compatible.
    """

    def __init__(self, simulator: Simulator, world, use_sim_time=True):
        self._simulator = simulator
        self._world = world
        self._use_sim_time = use_sim_time
        super().__init__()

    def start(self):
        """Start the simulation.
        
        Multiple simulations can be started at the same time. This is a 
        blocking call, it will block until the Simulator is successfully 
        started.
        
        Internally, this creates a new docker container containing the 
        Simulator, World, and Robot needed for the simulation. Once the 
        container is started, fido will create a persistent connection with 
        the ROS master running in the container.
        """
        try:
            self._simulator.start()
        except SimulatorError as exc:
            raise raise_from(SimulationError("failed to start simulation"), exc)

    def stop(self):
        """Stop the simulation.
        
        This will pause the simulator engine. Note that this is not sufficient 
        to end the simulation completely, this merely pauses the simulation. 
        To end a simulation, use `fido.simulation.Simulation.destroy()`. It is 
        not necessary to call stop() before destroy().
        """
        try:
            self._simulator.stop()
        except SimulatorError as exc:
            raise raise_from(SimulationError("failed to stop simulation"), exc)

    def reset(self):
        """Reset the simulation.
        
        This will cause the simulation to reset itself to its original state. 
        It allows the simulation to reset without doing a destroy() and 
        start(). This is useful in machine learning applications where each 
        iteration requires a fresh state.

        The exact reset behavior depends on the underlying simulator 
        implementation.
        """
        try:
            self._simulator.reset()
        except SimulatorError as exc:
            raise raise_from(SimulationError("failed to reset simulation"), exc)

    def destroy(self):
        """Destroy the simulation.
        
        This will destroy the container containing the simulation. Once the 
        simulation is destroyed, it can never be started again.
        """
        pass

    def view(self):
        """Visualize the simulation.
        
        This will display the simulation in a IPython.core.display.display. 
        This is compatible with Jupyter notebook.
        """
        try:
            self._simulator.view()
        except SimulatorError as exc:
            raise raise_from(SimulationError("failed to view simulation"), exc)

    def time(self):
        """Returns the simulation time.
        
        This can be either simulator time or wall time depending on the 
        `use_sim_time` flag on creation.
        """
        try:
            return self._simulator.time()
        except SimulatorError as exc:
            raise raise_from(SimulationError("failed to get simulation time"), exc)
