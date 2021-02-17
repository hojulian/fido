from future.utils import raise_from

from ..core import _ros_client
from ..errors import SimulatorError
from .simulator import Simulator


class Gazebo(Simulator):
    """Represents a Gazebo simulator.
    """

    def __init__(self):
        super().__init__()

    def start(self):
        pass

    def stop(self):
        pass

    def reset(self):
        pass

    def shutdown(self):
        pass

    def view(self):
        pass

    def time(self):
        pass
