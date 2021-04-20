import os
from abc import ABC, abstractmethod

from roslibpy import Ros

from ..errors import NotImplementedError, WorldError
from ..ros import InstallFile, LaunchFile


class World(ABC):
    """Represents a world.

    Currently this is only compatible with Gazebo.
    """

    _install_file: InstallFile
    _launch_file: LaunchFile

    _robots: list

    def __init__(self):
        self._install_file = InstallFile()
        self._launch_file = LaunchFile("simulation")
        self._robots = []
        self.__include_ros_bridge()

    def add(self, robot, x, y, z):
        """Add a robot to the world.

        Internally, this is converted into a gazebo_ros spawn_model
        call.
        """
        # Set robot initial position
        setattr(robot, "x", x)
        setattr(robot, "y", y)
        setattr(robot, "z", z)

        # Add robot dependency to install file
        robot.ros_fill_dependency(self._install_file)

        # Add robot to launch file
        self._launch_file.param(
            f"{robot.name}_robot_description", robot.ros_robot_description()
        )
        self._launch_file.node(
            "gazebo_ros",
            "spawn_model",
            f"spawn_{robot.model_name}",
            {
                "urdf": "",
                "model": robot.model_name,
                "x": x,
                "y": y,
                "z": z,
                "param": f"{robot.name}_robot_description",
            },
        )

        self._robots.append(robot)
        robot.set_world(self)

    def __include_ros_bridge(self):
        self._launch_file.include(
            "$(find rosbridge_server)/launch/rosbridge_websocket.launch",
            {
                "port": "9090",
            },
        )
        self._launch_file.node(
            "tf2_web_republisher",
            "tf2_web_republisher",
            "tf2_web_republisher",
        )

    def prepare_robots(self):
        """Prepare robots add ros client to each of the robots are initialize the
        internal sensors.
        """
        for r in self._robots:
            r.prepare()

    def set_simulation(self, simulation):
        self._simulation = simulation

    def remove(self, robot):
        """Remove a robot from the world.

        Internally, this is converted into a gazebo_ros delete_model
        call.
        """
        raise WorldError(
            "failed to call method on abstract world"
        ) from NotImplementedError("remove() not implemented")

    def robots(self):
        """Returns a list of robots."""
        return self._robots

    def ros(self):
        return self._simulation.ros()

    def export_files(self, path, package):
        """Export files to a given file.

        Internally, .rosinstall file is exported to the root of the directory.
        The launch file is exported to $PATH/src/$PACKAGE/launch.
        """
        self._install_file.to_file(path)
        self._launch_file.to_file(os.path.join(path, "src", package, "launch"))
