---
sidebar_label: errors
title: fido.errors
---

## Error

```python
class Error(Exception)
```

A generic error that is raised when Fido execution fails.

Whenever possible, the session will raise a more specific subclass of
`Error` from the `fido.errors` module.

### \_\_init\_\_

```python
 | def __init__(msg: str)
```

Creates a new `Error` indicating that an error has occurred.

**Arguments**:

- `msg` _str_ - The message string describing the error.

### msg

```python
 | @property
 | def msg() -> str
```

The error message that describes the error.

## RobotError

```python
class RobotError(Error)
```

Represents a robot error raised by the underlying robot.

This is a wrapper around any error raised by `fido.robot.Robot`.

## SimulationError

```python
class SimulationError(Error)
```

Represents a simulation error by the underlying simulation framework.

This is a wrapper around any error raised by `fido.simulation.Simulation`.

## SimulatorError

```python
class SimulatorError(Error)
```

Represents a simulator error by the underlying simulator.

This is a wrapper around any error raised by `fido.simulation.Simulator`.

## WorldError

```python
class WorldError(Error)
```

Represents a world error raised by the underlying world.

This is a wrapper around any error raised by `fido.world.World`.

## DockerError

```python
class DockerError(Error)
```

Represents a docker error raised by the underlying docker client.

This is a wrapper around any error raised by the internal docker client.

## DTypeError

```python
class DTypeError(Error)
```

Represents an error for dType.

