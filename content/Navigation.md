(navigation)=
# Navigation

The navigation stack of this robot is responsible for two main tasks: mapping and coverage. During mapping, the robot builds a representation of the environment from sensor data so that it can plan safe trajectories. During coverage, it generates a sequence of waypoints that traverses the free space while avoiding obstacles.

## Mapping

Before the robot can navigate properly through the environment and ensure proper coverage, the environment must first be known. That is where mapping approaches can be helpful. Several advanced and specialised mapping approaches already exist, but in this work only one was considered: frontier-based mapping. Frontier-based mapping allows the robot to start navigating the environment and expand its map as new areas are discovered, which is well suited to partially known indoor spaces [@SlamTBX2021].

For the actual motion execution, Nav2 is used as the low-level navigation framework. The coverage planners implemented in this work generate the waypoints that define the desired path, while Nav2 handles trajectory generation, obstacle avoidance, and execution of the motion in the live costmap [@macenski2020marathon2]. This separation keeps the higher-level planning logic simple while allowing the robot to respond to dynamic obstacles in real time.
