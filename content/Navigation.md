# Navigation
The navigation stack of this robot executes three main tasks:
- Mapping
- Patrolling
- Object Approach

## Mapping
Before the robot can navigate properly through the environment and ensure proper coverage, this environment must first be known. Thats where mapping approaches come in handy. Several advanced and specialized mapping approaches exist already, but in this paper only three are considered. Frontier based mapping, {2}, {3}. These were chosen through a combination of novelty and frequent application in similar contexts. Once the environment is mapped {sufficiently} the robot is allowed to navigate the space and propagate its behavior further down the tree.

### Coverage Planners

**Free space:**
The ROS framework allows for integration with a lot of modular software packages. throughout the years this has given rise to many universally applied packages, Nav2 is such a case.
Using Nav2 the Global Costmap can be used to extrapolate the free space for the robot to move in.

**Boustrophedon Coverage Planning**

**Coverage Path Planning with Morphological Skeleton Maps**

**Spanning Tree Coverage**

**Frontier Based Exploration**
