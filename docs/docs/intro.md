# Introduction

## Disclaimer

Fido is **still in development** but most of the functionalities are there.

## Overview

Fido makes it easy for beginners and experts to create end-to-end robot simulation
and control.

Similar to Jyro, a Python-based robot simulation library, this project provides an API
for robot control, model building, and simulation creation.

Fido is developed as an independent study project at Brandeis University for robotics 
education.

## Features

- Simulation
  - World Creation
  - Simulator control
- Robot control
  - Sensors feedback

## Using Fido

Here's a taste of Fido:

```python
from fido.robot import Turtlebot3
from fido.simulation import Gazebo, Simulation
from fido.world import RaceTrack

robot = Turtlebot3("bot_01")
world = RaceTrack()
world.add(robot, x=0, y=0, z=0)

sim = Simulation(
    simulator=Gazebo(gui=True),
    world=world,
)

sim.start()

robot.move(speed=2.0, duration=5.0)
robot.stop()

sim.stop()
sim.destroy()
```
