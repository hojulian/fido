"""Line follower example.

Taken from https://github.com/campusrover/prrexamples/blob/710eeb44dd27911aef63239900b030f193a71b66/src/follower_p.py
"""

import os
import sys

import cv2
import numpy as np

from fido.robot import Turtlebot3
from fido.simulation import Gazebo, Simulation
from fido.world import RaceTrack


def main():
    try:
        robot = Turtlebot3("follower_01")
        world = RaceTrack()

        world.add(robot)

        sim = Simulation(simulator=Gazebo(), world=world)
        sim.start()

        logcount = 0
        while True:
            # Get image from camera
            image = robot.image

            # Filter out everything that's not yellow
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            lower_yellow = np.array([40, 0, 0])
            upper_yellow = np.array([120, 255, 255])
            mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
            masked = cv2.bitwise_and(image, image, mask=mask)

            # Clear all but a 20 pixel band near the top of the image
            h, w, d = image.shape
            search_top = 3 * h / 4
            search_bot = search_top + 20
            mask[0:search_top, 0:w] = 0
            mask[search_bot:h, 0:w] = 0
            cv2.imshow("band", mask)

            # Compute the "centroid" and display a red circle to denote it
            M = cv2.moments(mask)
            logcount += 1
            print("M00 %d %d" % (M["m00"], logcount))

            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"]) + 100
                cy = int(M["m01"] / M["m00"])
                cv2.circle(image, (cx, cy), 20, (0, 0, 255), -1)

                # Move at 0.2 M/sec
                # add a turn if the centroid is not in the center
                # Hope for the best. Lots of failure modes.
                err = cx - w / 2
                robot.move(speed=0.2)
                robot.rotate(angle=-float(err) / 10)
            cv2.imshow("image", image)

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
