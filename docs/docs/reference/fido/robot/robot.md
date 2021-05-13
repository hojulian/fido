---
sidebar_label: robot
title: fido.robot.robot
---

## Robot

```python
class Robot(ABC,  RobotProtocol)
```

Represents a physical or simulated robot.

### add\_sensor

```python
 | def add_sensor(sensor_cls: Type["Sensor"], sensor_args: Mapping[str, Any] = {}) -> None
```

Add sensor to the robot.

**Arguments**:

- `sensor_cls` _Type[Sensor]_ - Sensor class.
- `sensor_args` _dict_ - Arguments mapping for initializing sensor.

### prepare

```python
 | def prepare() -> None
```

Prepare initializes all the sensors in the robot.

### connect

```python
 | def connect(host: str, port: int) -> None
```

Connect to the robot via ROS bridge.

**Arguments**:

- `host` _str_ - Name or IP address of the ROS bridge host, e.g. `127.0.0.1`.
- `port` _int_ - ROS bridge port, e.g. `9090`.

### ros

```python
 | def ros() -> Ros
```

Return internal ROS client.

**Returns**:

  The ROS client.

### set\_world

```python
 | def set_world(world: "World") -> None
```

Set the world to use for this robot.

**Arguments**:

- `world` _World_ - Parent world.

### move

```python
 | @abstractmethod
 | def move(distance: float = 0, duration: float = 0, speed: float = 0) -> None
```

Move the robot at a certain distance at a certain speed or for a
certain duration.

To move backwards, set speed to negative. If the given speed is
larger than the maximum speed, it will be set to the maximum
speed.

**Arguments**:

- `distance` _float_ - Distance to travel.
- `duration` _float_ - Time duration to travel for (in seconds).
- `speed` _float_ - Travel speed.

### rotate

```python
 | @abstractmethod
 | def rotate(angle: float = 0, duration: float = 0, speed: float = 0) -> None
```

Rotate the robot at a certain angle at a certain speed or for a
certain duration.

To rotate clockwise, set the speed to positive. To rotate in
anti-clockwise, set the speed to negative. If the given speed is
larger  than the maximum speed, it will be set to the maximum
speed.

**Arguments**:

- `angle` _float_ - Angle to rotate (in degrees).
- `duration` _float_ - Time duration to rotate for (in seconds).
- `speed` _float_ - Rotation speed (radian per seconds).

### stop

```python
 | @abstractmethod
 | def stop(forced: bool = False) -> None
```

Stop the robot.

This is a blocking call. It will block execution until the robot
is gracefully stopped unless `forced` is set to `True`.

**Arguments**:

- `forced` _bool_ - Forcefully stop the robot or not.

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
 | def ros_fill_dependency(installfile: "InstallFile") -> None
```

Fill the needed dependencies to the given installfile.

E.g. `installfile.git(
"src/turtlebot3",
"https://github.com/ROBOTIS-GIT/turtlebot3.git",
"master",
)`

**Arguments**:

- `installfile` _InstallFile_ - InstallFile for filling dependencies.

