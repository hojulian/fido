---
sidebar_label: dtypes
title: fido.dtypes.dtypes
---

## DType

```python
class DType(Protocol)
```

Represents the type of the element used by sensors and components.

It is implemented as a wrapper around common ROS messages.

## Odom

```python
class Odom(DType)
```

Represents a odometry state.

This is equivalent to ROS's nav_msgs/Odometry.

## Twist

```python
@dataclass(repr=True)
class Twist(DType)
```

Represents a twist message.

This is equivalent to ROS's geometry_msgs/Twist.

## LaserScan

```python
@dataclass(frozen=True, repr=True)
class LaserScan(DType)
```

Represents a laser scan in 360 degrees.

This is equivalent to ROS's sensor_msgs/LaserScan.

## Image

```python
@dataclass(frozen=True, repr=True)
class Image(DType)
```

Represents an image.

This is equivalent to ROS's sensor_msgs/Image.

