# Materials

## Hardware specifications
% Hieronder later nog goede lijsten van maken, stop het in de Github en verwijs ernaar zodat het minder ruimte opneemt in het verslag.\
The majority of hardware used in this implementation of the MIRTE Master stems from the standardized components implemented by the MIRTE team, which is what this section aims to specify. \
Mecanum wheels x4\
Orange Pi 3B V1.1.1\
MIRTE custom PCB\
Raspberry Pi Pico H\
12V 107 RPM motor x4\
Button\
OLED Display\
Gripper servo motors x5\
Raspberry Pi camera module\


Some parts had to be 3D-printed as the MIRTE team, at the time, did not have the capacity to provide these specific components. These include:
DC motor brackets\
Chassis side components\
Chassis rear sonar components\
Chassis front camera mount\
Chassis battery coupling component\
All gripper components\



## Software specifications

The MIRTE Master robotic platform has free open-source software available for any user to install. \
The latest stable release is used in this robotic system. This software comes packaged inside a ROS application {cite:t}`ROS2202`, a standardized framework for developing distributed robotic systems. This allows for the use of a wide variety of cross-compatible plugins and additional software packages, making rapid prototyping and development more efficient.

The particular ROS distribution the Mirte Master robot implements is ROS2 Humble Hawksbill on Ubuntu 22.04.

### Slam

Before the robot is able to perform any complex task in an environment, the environment must first be mapped. For this we use SLAM (Simultaneous Localization and Mapping). This way the robot can dynamically update its environment based on measurements from its Lidar scanner.
The robot created an occupancy grid map as an image while estimating the robot's pose.

To implement SLAM into the Mirte Master robot, SLAM Toolbox is used {cite:t}`SlamTBX2021`. This software package was chosen due to its native ROS2 support and good integration with other ROS2 packages. Slam toolbox allows for straight forward modification of mapping behavior using a set of parameters. In the case of the Mirte master, There have been several projects that have implemented slam toolbox, so a ready to use set of parameters for this robot is relatively easy to find. For this system, we use the [mirte navigation](https://github.com/MartijnWisse/mirte_navigation) ROS package from GitHub which provides ready-to-use configuration files and SLAM parameter settings.
It was assumed the robot would only navigate in unknown environments without predefined or reocurring maps. Therefore localization (using amcl) was disabled in the application.

### Navigation
>
> NAV2

### Manipulation

While the arm on the mirte master can be controlled in joint-space, our implementation \ relies on task-space (cartesian-space) control over the end effector position. \
The manner in motion planners are typically implemented requires the integration of several comlpex subsystems like inverse and forward kinematic solvers, trajectory planners and path planners. To accomplish the goal of task space control over the arm, we use MoveIt 2 {cite:t}`Coleman2014MoveIt`.

### Vision
