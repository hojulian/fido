---
sidebar_label: turtlebot3
title: fido.robot.turtlebot3
---

## Turtlebot3

```python
class Turtlebot3(Robot)
```

Represents a Turtlebot3 Burger robot.

For details about this robot, see:
https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/.

### move

```python
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
 | def stop(forced: bool = False) -> None
```

Stop the robot.

This is a blocking call. It will block execution until the robot
is gracefully stopped unless `forced` is set to `True`.

**Arguments**:

- `forced` _bool_ - Forcefully stop the robot or not.

### ros\_robot\_description

```python
 | def ros_robot_description() -> str
```

Return the ROS specific robot description.

This is mainly used for building the launch file. E.g.
`robot_description/urdf/model.urdf`.

**Returns**:

  The robot_description used by the launch file.

### ros\_fill\_dependency

```python
 | def ros_fill_dependency(installfile: "InstallFile") -> None
```

Fill the needed dependencies to the given installfile.

**Arguments**:

- `installfile` _InstallFile_ - InstallFile for filling dependencies.

