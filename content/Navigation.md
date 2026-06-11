# Navigation

The navigation stack of this robot is responsible for two main tasks:
- Mapping
- Coverage

### Mapping
Before the robot can navigate properly through the environment and ensure proper coverage, this environment must first be known. That is where mapping approaches can be helpful. Several advanced and specialised mapping approaches already exist, but in this paper only one was considered: 'frontier based mapping'. Once the environment is mapped sufficiently, the robot is allowed to navigate the space and propagate its behavior further down the tree.