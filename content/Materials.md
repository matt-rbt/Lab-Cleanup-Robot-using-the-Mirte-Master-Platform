# Materials
Within this section, all hardware employed within the MIRTE Master will be displayed and discussed.

## Hardware Specifications
The majority of the hardware used for this implementation of the MIRTE Master stems from the standard components implemented by the MIRTE team. Within this [Materials](https://matt-rbt.github.io/Lab-Cleanup-Robot-using-the-Mirte-Master-Platform/materials/) section, below, the list of all hardware parts can be seen, excluding only trivial components such as nuts and bolts.

| Category | Components |
|---|---|
| **Chassis** | |
| | _Panels:_ |
| | - Left (with OLED-display) and right chassis side panels (3D-printed) |
| | - Rear battery bracket panel (3D-printed) |
| | - 2x rear Sonar-module panel (3D-printed) |
| | - Front RGB-D camera module (3D-printed) |
| | - 1.5 mm aluminium: top plate, bottom plate and manipulator-mounting plate (laser-cut) |
| | |
| | _Electronics:_ |
| | - Main computer: Orange Pi 3B V1.1.1 |
| | - Microcontroller: Raspberry Pi Pico H |
| | - MIRTE custom PCB |
| | - Micro-SD-card |
| | - 12V RGB LED-strip |
| **Manipulation** | |
| | - Upper arm limb, lower arm limb (3D-printed) |
| | - Schoulder joint bracket, wrist joint bracket (3D-printed) |
| | - Double gears, bars for 4-bar linkage of gripper, triangle tips for gripper, TPE gripper ends (3D-printed) |
| | - Mounting bracket for RGB-camera module (3D-printed) |
| | - 5x Hiwonder bus servo-motors |
| | - Ball bearing for shoulder rotation joint |
| **Powertrain** | |
| | - Parkside 12V 5Ah Li-ion battery |
| | - Battery-to-circuit connector (3D-printed) |
| | - 12V to 5V step-down converter |
| | - Wiring, connectors, button and fuse |
| **Locomotion** | |
| | - 4x geared DC-motors |
| | - 4x mecanum wheels |
| | - 4x DC-motor brackets (3D-printed) |
| **Distance sensors** | |
| | - 2D-LiDAR: RPLiDAR C1 |
| | - 2x Ultrasonic sensor: HC-SR04 |
| **Cameras** | |
| | - RGBD (depth) camera: Orbbec3D Astra Mini S |
| | - RGB-camera: 720p USB camera module |

Given that MIRTE doesn't work with large quantities of robots, meaning no standardized parts are available, 3D-printing was a viable choice to establish the necessary parts of the frame using (for this specific project slightly adjusted versions of) the CAD-models provided. These parts can be divided into two groups: chassis and manipulator.

## Chassis

The chassis consists of a top, bottom and manipulator-mounting plate, for which aluminium plates with a thickness of 1.5 mm were used, as well as several side panels. These side panels don't only act as chassis support elements but also as mounting components for several electronics parts. For both of these purposes, PETG was chosen as a good filament to use for 3D-printing the panels. This filament been used for this application due to its relatively high strength, in addition to having enough ductility, it is easy to print and is relatively cheap. The ductility not only makes the robot more resistant to impact due to it being less brittle, it also allows for some slight bending of the chassis which has the added benefit that the wheels are more likely to keep traction on the floor. \
The variant of PETG used for this project was translucent which, aside from being aesthetically pleasing, also enables the user to look at the status lights on the inside of the chassis. This would otherwise not have been possible due to the aluminium top and bottom plates. During printing, orange PETG accent lines have also been added to the robot for both aesthetic purposes and it standing out more to people walking by.

## Manipulator

The manipulator consists of several components that can be found within the list at the top of the [Materials](https://matt-rbt.github.io/Lab-Cleanup-Robot-using-the-Mirte-Master-Platform/materials/) webpage. This system can be divided into four groups: brackets, limbs, servo-motors and the gripping mechanism. Given that there are four servo-motors, the arm is defined to have four degrees of freedom to be able to reach all places around the robot. There is a fifth servo-motor mounted, but that only actuates the gripping mechanism and therefore doesn't add any degree of freedom to the system. All of this, including the chassis, can be seen in the interactive display near the bottom of the [Mechanical](https://matt-rbt.github.io/Lab-Cleanup-Robot-using-the-Mirte-Master-Platform/mechanical) overview page.

## Software Specifications

The MIRTE Master robotic platform has free open-source software available for any user to install. \
The latest stable release is used in this robotic system. This software comes packaged inside a ROS application {cite:t}`ROS2_2022`, a standardized framework for developing distributed robotic systems. This allows for the use of a wide variety of cross-compatible plugins and additional software packages, making rapid prototyping and development more efficient.

The particular ROS distribution the MIRTE Master platform implements is ROS2 Humble Hawksbill on Ubuntu 22.04.

### SLAM

Before the robot is able to perform any complex task in an environment, the environment must first be mapped. For this, SLAM (Simultaneous Localization and Mapping) is used. This way the robot can dynamically update its environment based on measurements from its LiDAR scanner.
The robot created an occupancy grid map as an image while estimating the robot's pose.

To implement SLAM into the MIRTE Master robot, SLAM Toolbox is used {cite:t}`SlamTBX2021`. This software package was chosen due to its native ROS2 support and good integration with other ROS2 packages. Slam Toolbox allows for straight forward modification of mapping behavior using the set of parameters it provides. In the case of the MIRTE Master, there are several projects that have implemented SLAM Toolbox, so finding a ready-to-use set of SLAM parameters for this robot is relatively simple. The [Mirte Navigation](https://github.com/MartijnWisse/mirte_navigation) ROS package is used for configuration files and SLAM parameter settings.
It was assumed the robot would only navigate in unknown environments without predefined or reoccurring maps. Therefore localization (using AMCL) was disabled in the application.

### Manipulation

While the arm on the MIRTE Master can be controlled in joint-space, the implementation relies on task-space (cartesian-space) control over the end effector position. \
The manner which in motion planners are typically implemented requires the integration of several complex subsystems like inverse and forward kinematic solvers, trajectory planners and path planners. To accomplish the goal of task-space control over the arm, MoveIt 2 {cite:t}`Coleman2014MoveIt` was used.

### Navigation

Robot navigation also has a challenge analogous to that of robot manipulation, namely that of workspace control. The robot must be able to navigate to or through a set of waypoints given in the coordinate system of the map, while also implementing a real-time controller for obstacle avoidance. Similar to Moveit 2, Nav2 is used as a solution to this problem {cite:t}`macenski2020marathon2`. Aside from path planning and real-time control, Nav2 also provides a [Costmap](https://docs.nav2.org/configuration/packages/configuring-costmaps.html).  

### Vision

