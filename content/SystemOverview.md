# System Design and Architecture

The setup consists of a mobile manipulator (MIRTE Master) tasked with autonomously exploring an indoor laboratory environment, identifying and localizing objects, distinguishing between electronics and other objects, and sorting these objects accordingly.

The main task of the robot can be categorized into three sub-domains. Namely: motion planning, perception and navigation.

{numref}`Figure {number} <fig-task_bins>` below showcases this decomposition.

```{figure} figures/Lab_Cleanup-Task Bins-4.drawio.*
:label: fig-task_bins
:alt: How each task fits into the whole system
```

A common approach in robotics for navigation- and perception-heavy tasks is to use a global behavior tree that describes the robot's actions in different situations. This system-level architecture, as shown in {numref}`Figure {number} <fig-global_tree>`, is used here to describe and execute the cleaning strategy. The Py Trees for ROS python package is used to implement a behaviour tree due to its high level of documentation, aswell as native support in ROS 2.

```{figure} figures/labcleantree.png
:label: fig-global_tree
:alt: Global behavior tree of the entire system
```

The behavior tree provides a hierarchical approach for coordinating navigation, perception, and cleaning actions. It also provides a clear structure for debugging. As can be seen in {numref}`Figure {number} <fig-global_tree>`, the robot first explores the environment, then pauses its coverage task when an object is detected, approaches the object, checks whether it is still visible, picks it up, and places it in the appropriate basket.