---
sidebar_label: world
title: fido.world.world
---

## World

```python
class World(ABC,  WorldProtocol)
```

Represents a world.

Currently this is only compatible with Gazebo.

### add

```python
 | def add(robot: "Robot", x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None
```

Add a robot to the world.

Internally, this will create the corresponding launch file instructions for
starting the given robot. The robot dependencies are added to the `.rosinstall`
file.

Once the files are added, the world is added to the robot as a parent.

**Arguments**:

- `robot` _Robot_ - Robot to be added.
- `x` _float_ - X position in the world.
- `y` _float_ - Y position in the world.
- `z` _float_ - Z position in the world.

### prepare\_robots

```python
 | def prepare_robots() -> None
```

Prepare prepares all the robots in the world.

### set\_simulation

```python
 | def set_simulation(simulation: "Simulation") -> None
```

Set the parent simulation.

**Arguments**:

- `simulation` _Simulation_ - Parent simulation.

### remove

```python
 | def remove(robot: "Robot") -> None
```

Remove a robot from the world.

Internally, this is converted into a gazebo_ros delete_model
call.

**Arguments**:

- `robot` _Robot_ - Robot to be removed.

### robots

```python
 | def robots() -> List["Robot"]
```

Returns a list of robots.

**Returns**:

  The list of robots in this world.

### ros

```python
 | def ros() -> "Ros"
```

Return internal ROS client.

**Returns**:

  The ROS client.

### export\_files

```python
 | def export_files(path: str, package: str, rosbridge_port: int) -> None
```

Export files to a given file.

Internally, `.rosinstall` file is exported to the root of the directory.
The launch file is exported to $PATH/src/$PACKAGE/launch.

**Arguments**:

- `path` _str_ - Path to export files.
- `package` _str_ - Name of simulation package. Name should only contains
  alphanumeric characters and underscores. Normally named as
  `fido_simulation`.
- `rosbridge_port` _int_ - Port number of rosbridge.

