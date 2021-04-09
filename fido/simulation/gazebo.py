from urllib.parse import urlencode, urlunparse

from IPython.display import IFrame

from ..core import Core
from ..errors import SimulatorError
from .simulator import Simulator


class Gazebo(Simulator):
    """Represents a Gazebo simulator."""

    def __init__(self, gui=True):
        super().__init__(gui)

    def start(self):
        """Start the simulator.

        This starts the clock of the simulator.
        """
        pass

    def stop(self):
        """Pause the simulator.

        This will stop the simulation time as well.
        """
        pass

    def reset(self):
        """Reset the simulator.

        This will cause the simulator to reset itself to its original state.
        It allows the simulator to reset without doing a destroy() and start().
        This is useful in machine learning applications where each iteration
        requires a fresh state.

        The reset behavior depends on the simulator’s implementation.
        """
        pass

    def shutdown(self):
        """Exit the simulator.

        This will cause the simulator to exit. An error will be raised if the
        simulator exited with a non-zero exit code.
        """
        pass

    def view(self):
        """Visualize the simulator view.

        This will display the view in a `IPython.core.display.display`. This is
         compatible with Jupyter notebook.

        Currently, there is no way to adjust the view just yet.
        """
        host = "localhost"
        port = "6080"
        query = urlencode(
            {
                "path": "vnc",
                "autoconnect": "true",
                "resize": "scale",
                "reconnect": "true",
                "show_dot": "true",
                "bell": "false",
                "view_only": "false",
            }
        )
        src = urlunparse(
            (
                "http",
                f"{host}:{port}",
                "/vnc.html",
                None,
                query,
                None,
            )
        )
        return IFrame(src, "100%", "600px")

    def time(self):
        """Return the simulator time."""
        pass
