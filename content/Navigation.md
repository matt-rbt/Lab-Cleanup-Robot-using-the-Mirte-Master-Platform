# Navigation

The navigation stack of this robot is responsible for two main tasks:
- Mapping
- Coverage

### Mapping
Before the robot can navigate properly through the environment and ensure proper coverage, this environment must first be known. That is where mapping approaches can be helpful. Several advanced and specialised mapping approaches already exist, but in this paper only one was considered: 'frontier based mapping'. Unlike less advanced alternatives, frontier based mapping allows the robot to start navigating the space and propagate its behavior further down the tree as soon as the environment is mapped sufficiently.
