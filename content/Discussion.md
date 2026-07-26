# Discussion

## Delays
We were caught in the middle of a platform migration to a new design. This migration happened at the time that a master's course started, which used up all of the available MIRTE Master robots. This meant that, for us, no robot was available from the start of the project. We also had no clarity about when a unit would be received and whether additional components needed to be ordered, and we could not order all components ourselves because of budget restrictions. In the end, the components were received in week 13 of the 16-week project period. While the software team was able to frontload much of the development using Gazebo simulations, this still meant that the team had only three weeks to discover the quirks of the MIRTE Master, troubleshoot them, and integrate the software, which severely limited our ability to perform real-world quantitative and qualitative experiments.

## Gazebo
Gazebo was a useful tool for testing the software stack quickly and in an isolated manner. However, learning to work with Gazebo required a steep learning curve and a significant amount of additional effort to set up a realistic environment, including custom worlds and interactable objects.

When transferring the code base from the simulation environment to the real world, several problems occurred. The code had to be adjusted, for example by avoiding `use_sim_time`, and the robot's sensors were found to provide less accurate and less reliable feedback than expected.

## The MIRTE Master Platform
The MIRTE Master proved to be a viable starting platform for a cleaning robot. A lot of things were already largely configured: MoveIt was available, Nav2 for MIRTE was present, Gazebo already existed, and many of the configuration files and calibrations were operational.

However, some parts of the design were not tested as thoroughly as expected before integration within the MIRTE Master platform. The most significant issues were found in the perception components. The RGB-D camera was initially mounted near the front and lower part of the robot, which resulted in depth images that were not suitable for point-cloud processing. The included USB camera module was also excluded from the final design because of poor performance, including motion blur and a pronounced drop in frame rate under changing lighting conditions.

The final major issue encountered was time synchronization between the MIRTE Master and other machines. The OrangePi 3B on the MIRTE Master was not powerful enough to run the full software stack on its own, so much of the processing had to be offloaded to a laptop. For this to work correctly, the time needed to be synchronized between the devices. Later, a custom implementation based on [Chrony](https://chrony-project.org/) was used to synchronize the clocks automatically within acceptable tolerances.

In addition, the implemented navigation and perception approaches were feasible but not yet fully optimized. The coverage planners traded off completeness against path smoothness, and the perception pipeline remained sensitive to lighting and object appearance. These limitations provide useful guidance for future work.