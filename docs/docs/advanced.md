# Advanced Features

## Simulation

### Custom Docker Image

By default, simulation uses [`cosi119/fido-simulation:base`](https://github.com/hojulian/fido-image/blob/master/base/Dockerfile) as the base image. This image includes all the needed tools for running a simulation with the Gazebo simulator.

Base image's configuration:

- Ubuntu 18.04
- ROS Melodic
- NoVNC @ port 6080

You can implement your own custom image by extending the base image:

```dockerfile title="Dockerfile"
FROM cosi119/fido-simulation:base

# ...
```

## World

### Custom World

Fido supports custom worlds. To create a world, simply implements [`World`](./reference/fido/world/world).

See [`RaceTrack`](./reference/fido/world/racetrack) for an example implementation.

## Robot

### Custom Robot

Fido supports creation of custom robots. To create a robot, simply implements [`Robot`](./reference/fido/robot/robot). For a robot to be ROS compatible, it should also implements [`RobotProtocol`](./reference/fido/ros/protocol#robotprotocol-objects).

See [`Turtlebot3`](./reference/fido/robot/turtlebot3) for an example implementation.
