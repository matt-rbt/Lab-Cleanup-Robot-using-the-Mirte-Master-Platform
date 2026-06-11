# System Overview

The setup consists of a mobile manipulator (MIRTE Master) tasked with autonomously exploring an indoor laboratory environment, identifying and localizing objects, distinguishing between electronics and other objects and sorting these objects accordingly.

The main task of the robot can be broken down into sub-tasks, these then fit into specific niches of the entire system architecture:
1. **Motion planning**
2. **Perception**
3. **Navigation**
\
{numref}`Figure {number} <fig-task_bins>` below showcases this idea.

```{figure} figures/task_bins.*
:label: fig-task_bins
:alt: How each task fits into the whole system
```

The scope of this project includes how different mapping, navigation and perception approaches influence the performance of the whole system. The highest performing combination of approaches is then chosen for use in the respective subsystems.

The system level strategy dictates how the robot behaves in a given situation. The tasks described above are used as a guideline to construct the full system level strategy. The standard in robotics for such navigation and perception heavy tasks is to use a global behavior tree that describes how the robot ought to behave. This system level architecture, as shown in {numref}`Figure {number} <fig-global_tree>`, is also used here to describe and execute the actual cleaning strategy.

```{figure} figures/global_tree.*
:label: fig-global_tree
:alt: Global Behavior tree of the entire system
```

The behavior tree provides a hierarchical approach for coordinating navigation, perception and cleaning actions, cascades through the modules. It also can easily be visualised, simplifying debugging significantly. As can be seen from the tree, the robot will initially drive around. When it detects an object, it will approach, pick it up and place it in the correct basket.