# Navigation

The navigation stack of this robot is responsible for three main tasks:
- Mapping
- Coverage
- Object Approach

### Mapping
Before the robot can navigate properly through the environment and ensure proper coverage, this environment must first be known. Thats where mapping approaches come in handy. Several advanced and specialized mapping approaches exist already, but in this paper only one was considered. Frontier based mapping. Once the environment is mapped {sufficiently} the robot is allowed to navigate the space and propagate its behavior further down the tree.