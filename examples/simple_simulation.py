import os
import sys

from fido.simulation import Simulation, Gazebo
from fido.world import RaceTrack
from fido.robot import Turtlebot3


def main():
    try:
        robot = Turtlebot3("bot_01")
        world = RaceTrack()
        world.add(robot, x=0, y=0, z=0)

        sim = Simulation(
            simulator=Gazebo(gui=True),
            world=world,
        )
        sim.start()
        sim.view()
        # robot.start()

    except KeyboardInterrupt as exc:
        robot.stop(forced=True)
        sim.stop()
        sim.destroy()

        try:
            sys.exit(exc)
        except SystemExit:
            os._exit(exc)


if __name__ == "__main__":
    main()
