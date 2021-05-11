# Examples

## Moving and Rotating

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

# Move at speed 2.0 for 5.0s
robot.move(speed=2.0, duration=5.0)
robot.stop()

# Rotate for 45 degrees.
robot.rotate(angle=45.0, speed=2.0)

sim.stop()
sim.destroy()
```

## Physical control

```python
from fido.robot import Turtlebot3

robot = Turtlebot3("bot_01", physical=True)
robot.connect(host="127.0.0.1", port=9090)

# Move at speed 2.0 for 5.0s
robot.move(speed=2.0, duration=5.0)
robot.stop()
```
