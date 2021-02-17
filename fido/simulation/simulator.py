from future.utils import raise_from

from ..errors import SimulatorError, NotImplementedError


class Simulator(object):
    """Represents a simulator.
    
    A simulator provides a ROS compatible physics engine for running a 
    simulation. 
    
    Currently, there is only one supported simulator implementation: Gazebo.
    """

    def __init__(self):
        super().__init__()

    def start(self):
        """Start the simulator.
        
        This starts the clock of the simulator.
        """
        raise raise_from(
            SimulatorError("failed to call method on abstract simulator"),
            NotImplementedError("start() not implemented"),
        )

    def stop(self):
        """Pause the simulator.
        
        This will stop the simulation time as well.
        """
        raise raise_from(
            SimulatorError("failed to call method on abstract simulator"),
            NotImplementedError("stop() not implemented"),
        )

    def reset(self):
        """Reset the simulator.
        
        This will cause the simulator to reset itself to its original state. 
        It allows the simulator to reset without doing a destroy() and start(). 
        This is useful in machine learning applications where each iteration 
        requires a fresh state.

        The reset behavior depends on the simulator’s implementation.
        """
        raise raise_from(
            SimulatorError("failed to call method on abstract simulator"),
            NotImplementedError("reset() not implemented"),
        )

    def shutdown(self):
        """Exit the simulator.
        
        This will cause the simulator to exit. An error will be raised if the 
        simulator exited with a non-zero exit code.
        """
        raise raise_from(
            SimulatorError("failed to call method on abstract simulator"),
            NotImplementedError("shutdown() not implemented"),
        )

    def view(self):
        """Visualize the simulator view.
        
        This will display the view in a `IPython.core.display.display`. This is
         compatible with Jupyter notebook.

        Currently, there is no way to adjust the view just yet.
        """
        raise raise_from(
            SimulatorError("failed to call method on abstract simulator"),
            NotImplementedError("view() not implemented"),
        )

    def time(self):
        """Return the simulator time.
        """
        raise raise_from(
            SimulatorError("failed to call method on abstract simulator"),
            NotImplementedError("time() not implemented"),
        )
