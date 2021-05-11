import os
from abc import ABC
from typing import List

from roslibpy import Ros

from ..errors import NotImplementedError, WorldError
from ..robot import Robot
from ..ros import InstallFile, LaunchFile, WorldProtocol


class World(ABC, WorldProtocol):
    """Represents a world.

    Currently this is only compatible with Gazebo.
    """

    _install_file: InstallFile
    _launch_file: LaunchFile
    _robots: List[Robot]

    def __init__(self):
        self._install_file = InstallFile()
        self._launch_file = LaunchFile("simulation")
        self._robots = []
        self._included_rosbridge = False

    def add(self, robot: Robot, x=0, y=0, z=0) -> None:
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

    def __include_ros_bridge(self, rosbridge_port=9090):
        self._launch_file.include(
            "$(find rosbridge_server)/launch/rosbridge_websocket.launch",
            {
                "port": f"{rosbridge_port}",
            },
        )
        self._launch_file.node(
            "tf2_web_republisher",
            "tf2_web_republisher",
            "tf2_web_republisher",
        )

    def prepare_robots(self) -> None:
        """Prepare prepares all the robots in the world."""
        for r in self._robots:
            r.prepare()

    def set_simulation(self, simulation) -> None:
        """Set the parent simulation."""
        self._simulation = simulation

    def remove(self, robot: Robot) -> None:
        """Remove a robot from the world.

        Internally, this is converted into a gazebo_ros delete_model
        call.
        """
        raise WorldError(
            "failed to call method on abstract world"
        ) from NotImplementedError("remove() not implemented")

    def robots(self) -> List[Robot]:
        """Returns a list of robots."""
        return self._robots

    def ros(self) -> Ros:
        """Return internal ROS client."""
        return self._simulation.ros()

    def export_files(self, path, package, rosbridge_port) -> None:
        """Export files to a given file.

        Internally, .rosinstall file is exported to the root of the directory.
        The launch file is exported to $PATH/src/$PACKAGE/launch.
        """
        if not self._included_rosbridge:
            self.__include_ros_bridge(rosbridge_port)
            self._included_rosbridge = True

        self._install_file.to_file(path)
        self._launch_file.to_file(os.path.join(path, "src", package, "launch"))
