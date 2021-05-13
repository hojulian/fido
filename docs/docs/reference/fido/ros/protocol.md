---
sidebar_label: protocol
title: fido.ros.protocol
---

## RobotProtocol

```python
class RobotProtocol(Protocol)
```

RobotProtocol is implemented by a robot that is ROS compatible.

### connect

```python
 | @abstractmethod
 | def connect(host: str, port: int) -> None
```

Connect to the robot via ROS bridge.

**Arguments**:

- `host` _str_ - Name or IP address of the ROS bridge host, e.g. `127.0.0.1`.
- `port` _int_ - ROS bridge port, e.g. `9090`.

### ros\_robot\_description

```python
 | @abstractmethod
 | def ros_robot_description() -> str
```

Return the ROS specific robot description.

This is mainly used for building the launch file. E.g.
`robot_description/urdf/model.urdf`.

**Returns**:

  The robot_description used by the launch file.

### ros\_fill\_dependency

```python
 | @abstractmethod
 | def ros_fill_dependency(installfile: InstallFile) -> None
```

Fill the needed dependencies to the given installfile.

E.g.

```python
installfile.git(
    "src/turtlebot3",
    "https://github.com/ROBOTIS-GIT/turtlebot3.git",
    "master",
)`
```

**Arguments**:

- `installfile` _InstallFile_ - InstallFile for filling dependencies.

### ros

```python
 | @abstractmethod
 | def ros() -> "Ros"
```

Return internal ROS client.

**Returns**:

  The ROS client.

## WorldProtocol

```python
class WorldProtocol(Protocol)
```

WorldProtocol is implemented by a world that is ROS compatible.

### ros

```python
 | @abstractmethod
 | def ros() -> "Ros"
```

Return internal ROS client.

**Returns**:

  The ROS client.

## SimulatorProtocol

```python
class SimulatorProtocol(Protocol)
```

SimulatorProtocol is implemented by a simulator that is ROS compatible.

### ros

```python
 | @abstractmethod
 | def ros() -> "Ros"
```

Return internal ROS client.

**Returns**:

  The ROS client.

