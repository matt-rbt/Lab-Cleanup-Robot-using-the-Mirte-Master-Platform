# Manipulation

This section covers the articulation of the robotic arm that sits atop the MIRTE Master. Since there is hardly any competition in the space, the market leader, MoveIt 2, will be used to move the arm. MoveIt 2 provides a well-documented API and directs the vast majority of computations regarding (inverse) kinematics of robotic arms and the trajectory planning thereafter ([source](https://moveit.picknik.ai/main/api/html/index.html)).

The package is already installed on the MIRTE Master and has previously been used semi-successfully to move MIRTE's arm ([source](https://docs.mirte.org/develop/doc/tutorials/moveit.html)). However, this implementation resulted in the end effector (the tip of the arm; the wrist) being positioned more than 10 cm off-target. For a machine needing to pick up objects smaller than 6 cm, this is unacceptable. Therefore, an improved version is required. To this end, the designed behaviour contains a multitude of improvements and concessions:

## Changes

- The previously missing configuration file, `moveit_cpp.yaml`, which contains additional parameters (specifically for OMPL, the motion planner), was created and added.

- To accommodate the fact that MIRTE's arm can only move with four degrees of freedom (DOF) instead of the six assumed by MoveIt 2, planning is performed strictly for position, ignoring any orientation component of a goal pose entirely. Together with the first point, this made it possible to use more precise methods from the Move Group Interface to plan and execute movements instead of `setApproximateJointValues()`. The resulting positional accuracy is in the order of millimetres, although alignment of the gripper must be configured separately.

- Functionality has been added to ensure that the gripper points downward with respect to the world axes as much as possible. This ensures that any approached object is directly below the wrist camera, which is responsible for classifying objects. As a result, the gripper camera has a constant and uniform background, increasing classification confidence levels.

- An action server has been developed that provides feedback to a potential action client. The server can receive goals in several formats:
  - By specifying the name of a predefined joint state defined in the robot's description files.
  - By supplying a goal pose relative to MIRTE's frame `base_link`.

  The action server moves the arm in a way that satisfies the goal, if possible. The wrist joint can be moved separately to allow fine adjustment of the gripper's orientation. Similarly, the gripper can be controlled either by specifying a named state or by directly assigning a desired clamping angle. The gripper will move accordingly, if possible.

Together, these modifications facilitate the movement of the robotic arm for this specific project and enable the creation of additional custom manipulation modules for future projects.