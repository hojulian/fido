import React from "react";
import clsx from "clsx";
import CodeBlock from "@theme-original/CodeBlock";
import styles from "./HomepageFeatures.module.css";

const FeatureList = [
  {
    title: "Simulated Robot",
    description: <>Fido makes it easy to control a robot in simulation.</>,
    code: `
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

    sim.stop()
    `,
  },
  {
    title: "Physical Robot",
    description: (
      <>Fido also supports controlling a physical robot in real-time.</>
    ),
    code: `
    from fido.robot import Turtlebot3

    robot = Turtlebot3("bot_01", physical=True)
    robot.connect(host="127.0.0.1", port=9090)

    # Move at speed 2.0 for 5.0s
    robot.move(speed=2.0, duration=5.0)
    robot.stop()
    `,
  },
];

function Feature({ title, description, code }) {
  return (
    <div className={clsx("col col--6")}>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
      <div>
        <CodeBlock className="python" title="" metastring="" children={code} />
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
