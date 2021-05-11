---
sidebar_label: sensor
title: fido.robot.component.sensor
---

## Sensor

```python
class Sensor(object)
```

Represents a sensor on the robot.

Internally, a sensor listens to a specific ROS topic and updates the robot&#x27;s
internal state. For instance, a Odomer listens to the /odom topic and update the
robot&#x27;s `x`, `y`, `z` coordinates. A sensor only starts listening to updates once
the simulation has started. It will stop updating once the simulation is destroyed.

### handle\_updates

```python
 | @abstractmethod
 | def handle_updates(ros: "Ros") -> Callable[[], None]
```

Handle incoming update from ROS topic and update robot&#x27;s state accordingly.

**Arguments**:

- `ros` _Ros_ - ROS client.
  

**Returns**:

  A callback for unsubscribing the topic.

## Odomer

```python
class Odomer(Sensor)
```

Represents an Odometry updater.

### handle\_updates

```python
 | def handle_updates(ros: "Ros") -> Callable[[], None]
```

Handle incoming update for `/odom` topic and update robot&#x27;s position
accordingly.

**Arguments**:

- `ros` _Ros_ - ROS client.
  

**Returns**:

  A callback for unsubscribing the topic.

## Lidar

```python
class Lidar(Sensor)
```

Represents a Lidar sensor.

### handle\_updates

```python
 | def handle_updates(ros: "Ros") -> Callable[[], None]
```

Handle incoming update for `/scan` topic and update robot&#x27;s ranges
accordingly.

**Arguments**:

- `ros` _Ros_ - ROS client.
  

**Returns**:

  A callback for unsubscribing the topic.

