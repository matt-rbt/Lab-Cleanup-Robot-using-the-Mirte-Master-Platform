## System level strategy

The setup consists of a mobile manipulator (Mirte Master) tasked with
autonomously exploring an indoor environment (the robotics lab), identifying and localizing objects, distinguishing between electronics and other objects, and sorting these objects accordingly. The task can be broken down as follows.

The main task of the robot can be broken down into sub-tasks which then fit into specific niches of the entire system architecture. **Motion planning**, **perception** and **navigation**. {numref}`Figure {number} <fig-task_bins>` showcases this idea.

```{figure} figures/task_bins.*
:label: fig-task_bins
:alt: How each task fits into the whole system
```

The scope of our investigation includes how different perception(classification) and navigation(mapping and patrolling) approaches influence the performance of the whole system. The highest performing combination of approaches is then chosen for use in the respective subsystems.

The system level strategy consists of how the robot behaves in each scenario that it will find itself. The tasks described above are used as a guideline to construct the full system level strategy. The standard in robotics for such navigation and perception heavy tasks is to use a global behavior tree that describes how the robot ought to behave in certain situations. This system level architecture as shown in {numref}`Figure {number} <fig-global_tree>` is also used here to describe and execute the cleaning strategy.

```{figure} figures/global_tree.*
:label: fig-global_tree
:alt: Global Behavior tree of the entire system
```
