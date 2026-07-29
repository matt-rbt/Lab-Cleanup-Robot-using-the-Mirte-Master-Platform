# Overview

The setup consists of a mobile manipulator (MIRTE Master) tasked with autonomously exploring an indoor laboratory environment, identifying and localizing objects, distinguishing between electronics and other objects, and sorting these objects accordingly.

To realize this, the robot incorporates several distinct, but tightly knit software subsystems. Each one is responsible for a separate function of autonomous operation, but simultaneously reliant on data from one or more of the other systems.

At the highest level sits a behavior tree that orchestrates how these different subsystems interact to make the robot execute the main goal. It decides when to explore, when to approach a detected object, when to classify it, and when to pick and place it.

Below this, a navigation system handles how the robot moves through the environment. It maps, then plans a coverage path, enabling the discovery of portable objects.
The manipulation system plans and executes pick and place motions given object poses and visibility.
Underpinning both is the perception pipeline, which provides the system with a continuous stream of object poses and classifications derived from depth and colour data.

These subsystems do not operate in isolation. The behavior tree depends on perception to make decisions, perception depends on navigation to bring the camera within range of objects, and manipulation depends on the localization estimates that perception provides. Understanding the system therefore requires understanding how these parts interact, not just what each part does individually.

The following sections describe each subsystem in turn: behavior and task orchestration, manipulation and motion planning, perception, and navigation.
