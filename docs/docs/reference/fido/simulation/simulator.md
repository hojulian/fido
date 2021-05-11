---
sidebar_label: simulator
title: fido.simulation.simulator
---

## Simulator

```python
class Simulator(ABC,  SimulatorProtocol)
```

Represents a simulator.

A simulator provides a ROS compatible physics engine for running a
simulation.

Currently, there is only one supported simulator implementation: Gazebo.

### set\_simulation

```python
 | def set_simulation(simulation: "Simulation") -> None
```

Set the parent simulation.

**Arguments**:

- `simulation` _Simulation_ - Parent simulation.

### start

```python
 | @abstractmethod
 | def start() -> None
```

Start the simulator.

This starts the clock of the simulator.

### stop

```python
 | @abstractmethod
 | def stop() -> None
```

Pause the simulator.

This will stop the simulation time as well.

### reset

```python
 | @abstractmethod
 | def reset() -> None
```

Reset the simulator.

This will cause the simulator to reset itself to its original state.
It allows the simulator to reset without doing a `destroy()` and `start()`.
This is useful in machine learning applications where each iteration
requires a fresh state.

The reset behavior depends on the simulator’s implementation.

### view

```python
 | @abstractmethod
 | def view() -> "IFrame"
```

Visualize the simulator view.

This will display the view in a `IPython.core.display.display`. This is
compatible with Jupyter notebook.

Currently, there is no way to adjust the view just yet.

### time

```python
 | @abstractmethod
 | def time() -> float
```

Return the simulator time.

**Returns**:

  The simulator time.

