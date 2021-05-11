---
sidebar_label: gazebo
title: fido.simulation.gazebo
---

## Gazebo

```python
class Gazebo(Simulator)
```

Represents a Gazebo simulator.

### start

```python
 | def start() -> None
```

Start the simulator.

This starts the clock of the simulator.

### stop

```python
 | def stop() -> None
```

Pause the simulator.

This will stop the simulation time as well.

### reset

```python
 | def reset() -> None
```

Reset the simulator.

This will cause the simulator to reset itself to its original state.
It allows the simulator to reset without doing a `destroy()` and `start()`.
This is useful in machine learning applications where each iteration
requires a fresh state.

In gazebo, reset will restart the entire simulation including the time.

### view

```python
 | def view() -> IFrame
```

Visualize the simulator view.

This will start a gazebo GUI using gzclient and display on the noVNC page. Then
the page is displayed as an IFrame using `IPython.core.display.display`. This is
compatible with Jupyter notebook.

Currently, there is no way to adjust the view just yet.

**Returns**:

  Gazebo GUI in an IFrame.

### time

```python
 | def time() -> float
```

Return the simulator time.

**Returns**:

  The simulator time.

### ros

```python
 | def ros() -> "Ros"
```

Return internal ROS client.

**Returns**:

  The ROS client.

