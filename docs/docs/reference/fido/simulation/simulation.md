---
sidebar_label: simulation
title: fido.simulation.simulation
---

## Simulation

```python
class Simulation(object)
```

Represents a single simulation.

A simulation is made out of two things: a world `fido.world.World` and a
simulator `fido.simulation.Simulator` for running the simulation.

Note that both the simulator and world need to be compatible.

When a Simulation is created, it will first initialize by loading all the external
world and robot files using rosinstall. Then, it will create a docker container with
the files attached to the catkin workspace. The container created will be in a pause
state. To start the container and simulation, call `start()`.

### start

```python
 | def start() -> None
```

Start the simulation.

Multiple simulations can be started at the same time. This is a
blocking call, it will block until the Simulator is successfully
started.

Internally, if the simulation is not initialized, it creates a new docker
container containing the `Simulator`, `World`, and `Robot` needed for the
simulation. Once the container is started, it will first build all the packages
in the directory using catkin_make. Then, fido will start the simulation by
launching the launch file on a separate thread. Once the launch file is ready,
fido will create apersistent connection with ROS master running in the container
using rosbridge.

If the simulation is initialized, it will simply call `start()` of the
underlying simulator.

### ros

```python
 | def ros() -> Ros
```

Returns the ros client.

**Returns**:

  The ROS client.

### stop

```python
 | def stop() -> None
```

Stop the simulation.

This will pause the simulator engine. Note that this is not sufficient
to end the simulation completely, this merely pauses the simulation.

To end a simulation, use `Simulation.destroy()`. It is not necessary
to call `Simulation.stop()` before `Simulation.destroy()`.

### reset

```python
 | def reset() -> None
```

Reset the simulation.

This will cause the simulation to reset itself to its original state.
It allows the simulation to reset without doing `Simulation.destroy()`
and `Simulation.start()`.

This is useful in machine learning applications where each iteration
requires a fresh state.

The exact reset behavior depends on the underlying simulator
implementation.

### destroy

```python
 | def destroy() -> None
```

Destroy the simulation.

This will forcefully destroy the container containing the simulation.

Once the simulation is destroyed, it can never be started again.

### view

```python
 | def view() -> "IFrame"
```

Visualize the simulation.

This will display the simulation in a `IPython.core.display.display()`.
This is compatible with Jupyter notebook.

### container\_id

```python
 | @property
 | def container_id() -> str
```

Return the docker container ID of this simulation.

This is used by simulator to execute command on the underlying docker container.

Although not recommended, this container ID can be used with docker-cli to
access and manage the simulation container.

### vnc\_port

```python
 | @property
 | def vnc_port() -> str
```

Return vnc port.

This is used by simulator for accessing the VNC viewport.

### time

```python
 | def time() -> float
```

Return the simulation time.

This can be either simulator time or wall time depending on the
`use_sim_time` flag on creation.

