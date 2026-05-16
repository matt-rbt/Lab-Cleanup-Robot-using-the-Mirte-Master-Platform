## Navigation
The navigation stack of this robot executes three main tasks:
- Mapping
- Coverage
- Object Approach

### Mapping
Before the robot can navigate properly through the environment and ensure proper coverage, this environment must first be known. Thats where mapping approaches come in handy. Several advanced and specialized mapping approaches exist already, but in this paper only three are considered. Frontier based mapping, {2}, {3}. These were chosen through a combination of novelty and frequent application in similar contexts. Once the environment is mapped {sufficiently} the robot is allowed to navigate the space and propagate its behavior further down the tree.

### Coverage

```{nbinclude} content/CoveragePlanners.ipynb
:hide-code: false
:hide-output: false```