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



Some parts had to be 3D-printed as, at the time, the MIRTE team did not have the capacity to provide these specific components. These include:
DC motor brackets\
Chassis side components\
Chassis rear sonar components\
Chassis front camera mount\
Chassis battery coupling component\
All gripper components\

The majority of hardware used for this implementation of the MIRTE Master stems from components designed by the MIRTE team, the corresponding list of items can be found here: [verwijzing naar lijst op de website]
Given that MIRTE doesn't work with large quantities of robots, meaning no standardized parts were available, 3D-printing was a viable choice to establish the necessary parts of the frame using (for this specific project slightly adjusted versions of) the CAD-models provided. The parts of which can be divided into two groups: chassis and manipulator.\

The chassis consists of a top and bottom plate, for which 1.5 mm thick aluminium was used, as well as several side panels. These side panels don't only act as chassis support elements but also as mounting components for several electronics parts. For both of these tasks, PETG was chosen as the filament to use for the 3D-printing of these panels. This filament is often a popular choice, and here it's been used due to it's relatively high strength and some ductility, compared to filaments like PLA that are more brittle. Not only does this mean that it is less likely to snap, but it also allows for some slight chassis bending which has as an added benefit that the wheels are more likely to keep traction.\

The manipulator consists of several components that can be found in this list: [verwijzen naar lijst op de website]. This system can be divided into four groups: brackets, limbs, servo-motors and the gripping mechanism. Given that there are four servo-motors, the arm is defined to have four degrees of freedom to be able to reach all places around the robot. There is a fifth servo-motor mounted, but that only actuates the gripping mechanism and therefore doesn't add any degree of freedom.\

The chassis side panels have been constructed using PETG of the translucent variety which, aside from being easthetically pleasing, allows some ability of looking at status lights on the inside of the robot. This otherwise wouldn't have been an possible due to the enclosure having aluminium top and bottom plates. Add to that, orange PETG strips have been printed within the PETG of both the chassis side panels and the manipulator limbs in order to make the robot stand out more, theoretically leading to people being more cautious around it while it's moving. All of this can be seen in the interactive display [verwijzen naar dat 3D model].

## Software specifications

The MIRTE Master robotic platform has free open-source software available for any user to install. \
The latest stable release is used in this robotic system. This software comes packaged inside a ROS application {cite:t}`ROS2202`, a standardized framework for developing distributed robotic systems. This allows for the use of a wide variety of cross-compatible plugins and additional software packages, making rapid prototyping and development more efficient.

The particular ROS distribution the MIRTE Master platform implements is ROS2 Humble Hawksbill on Ubuntu 22.04.

### Slam

Before the robot is able to perform any complex task in an environment, the environment must first be mapped. For this we use SLAM (Simultaneous Localization and Mapping). This way the robot can dynamically update its environment based on measurements from its LiDAR scanner.
The robot created an occupancy grid map as an image while estimating the robot's pose.

To implement SLAM into the MIRTE Master robot, SLAM Toolbox is used {cite:t}`SlamTBX2021`. This software package was chosen due to its native ROS2 support and good integration with other ROS2 packages. Slam toolbox allows for straight forward modification of mapping behavior using a set of parameters. In the case of the MIRTE Master, There have been several projects that have implemented SLAM Toolbox, so a ready to use set of parameters for this robot is relatively easy to find. For this system, we use the [mirte navigation](https://github.com/MartijnWisse/mirte_navigation) ROS package from GitHub which provides ready-to-use configuration files and SLAM parameter settings.
It was assumed the robot would only navigate in unknown environments without predefined or reoccurring maps. Therefore localization (using AMCL) was disabled in the application.

### Navigation
>
> NAV2

### Manipulation

While the arm on the MIRTE Master can be controlled in joint-space, the implementation relies on task-space (cartesian-space) control over the end effector position. \
The manner in motion planners are typically implemented requires the integration of several complex subsystems like inverse and forward kinematic solvers, trajectory planners and path planners. To accomplish the goal of task space control over the arm, MoveIt 2 {cite:t}`Coleman2014MoveIt` was used.

### Vision
