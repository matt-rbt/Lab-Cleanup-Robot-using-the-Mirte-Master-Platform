# Materials
Within this section, all materials within the MIRTE Master will be displayed and discussed.

## Hardware Specifications
% De lijst hieronder moet alleen op de website, niet in het verslag. Verwijs er wel naar in het verslag.

The majority of the hardware used for this implementation of the MIRTE Master stems from the standard components implemented by the MIRTE team. Below, the list of all hardware parts can be seen, excluding only trivial components such as nuts and bolts.

| Category | Components |
|---|---|
| **Chassis** | _Panels:_ |
| | - Left (with OLED-display) and right chassis side panels (3D-printed) |
| | - Rear battery bracket panel (3D-printed) |
| | - 2x rear Sonar-module panel (3D-printed) |
| | - Front RGB-D camera module (3D-printed) |
| | - 1.5 mm aluminium: top plate, bottom plate and manipulator-mounting plate (laser-cut) |
| | _Electronics:_ |
| | - Main computer: Orange Pi 3B V1.1.1 |
| | - Microcontroller: Raspberry Pi Pico H |
| | - MIRTE custom PCB |
| | - 12V RGB LED-strip |
| **Manipulation** | |
| | - Upper arm limb, lower arm limb (3D-printed) |
| | - Schoulder joint bracket, wrist joint bracket (3D-printed) |
| | - Double gears, bars for 4-bar linkage of gripper, tips for gripper, TPU gripper ends (3D-printed) |
| | - Mounting bracket for RGB-camera module (3D-printed) |
| | - 5x Hiwonder bus servo-motors |
| **Power system** | |
| | - Parkside 12v 5Ah Li-ion battery |
| | - Battery-to-circuit connector (3D-printed) |
| | - 12V to 5V step-down converter |
| | - Wiring, connectors, button and fuse |
| **Space traversing** | |
| | - 4x geared DC-motors |
| | - 4x mecanum wheels |
| | - 4x DC motor brackets (3D-printed) |
| **Navigation sensors** | |
| | - 2D-LiDAR: RPLiDAR C1 |
| | - 2x Ultrasonic sensor: HC-SR04 |
| **Vision sensors** | |
| | - Depth camera: Orbbec3D Astra Mini S |
| | - RGB-camera: 720p USB camera module |

Given that MIRTE doesn't work with large quantities of robots, meaning no standardized parts are available, 3D-printing was a viable choice to establish the necessary parts of the frame using (for this specific project slightly adjusted versions of) the CAD-models provided. These parts can be divided into two groups: chassis and manipulator.

## Chassis

The chassis consists of a top, bottom and manipulator-mounting plate, for which 1.5 mm thick aluminium was used, as well as several side panels. These side panels don't only act as chassis support elements but also as mounting components for several electronics parts. For both of these purposes, PETG was chosen as a good filament to use for 3D-printing these panels. This filament been used for this application due to its relatively high strength, in addition to having enough ductility, is easy to print and is relatively cheap. The ductility not only makes the robot more resistant to impact due to it being less brittle, it also allows for some slight bending of the chassis which has the added benefit that the wheels are more likely to keep traction on the floor. The variety of PETG used for this project was translucent which, aside from being aesthetically pleasing, also enables the user to look at the status lights on the inside of the chassis. This would otherwise not have been possible due to the aluminium top and bottom plates. During printing, orange PETG accent lines have also been added to the robot for both aesthetic purposes and it standing out more to people walking by.

## Manipulator

The manipulator consists of several components that can be found within the list at the top of the [Materials](https://matt-rbt.github.io/Lab-Cleanup-Robot-using-the-Mirte-Master-Platform/materials/) page. This system can be divided into four groups: brackets, limbs, servo-motors and the gripping mechanism. Given that there are four servo-motors, the arm is defined to have four degrees of freedom to be able to reach all places around the robot. There is a fifth servo-motor mounted, but that only actuates the gripping mechanism and therefore doesn't add any degree of freedom to the system. All of this, including the chassis, can be seen in the interactive display near the bottom of the [Mechanical](https://matt-rbt.github.io/Lab-Cleanup-Robot-using-the-Mirte-Master-Platform/mechanical) overview page.

## Software Specifications

The MIRTE Master robotic platform has free open-source software available for any user to install. \
The latest stable release is used in this robotic system. This software comes packaged inside a ROS application {cite:t}`ROS2202`, a standardized framework for developing distributed robotic systems. This allows for the use of a wide variety of cross-compatible plugins and additional software packages, making rapid prototyping and development more efficient.

The particular ROS distribution the MIRTE Master platform implements is ROS2 Humble Hawksbill on Ubuntu 22.04.

### Slam

Before the robot is able to perform any complex task in an environment, the environment must first be mapped. For this we use SLAM (Simultaneous Localization and Mapping). This way the robot can dynamically update its environment based on measurements from its LiDAR scanner.
The robot created an occupancy grid map as an image while estimating the robot's pose.

To implement SLAM into the MIRTE Master robot, SLAM Toolbox is used {cite:t}`SlamTBX2021`. This software package was chosen due to its native ROS2 support and good integration with other ROS2 packages. Slam toolbox allows for straight forward modification of mapping behavior using a set of parameters. In the case of the MIRTE Master, There have been several projects that have implemented SLAM Toolbox, so a ready to use set of parameters for this robot is relatively easy to find. For this system, we use the [Mirte Navigation](https://github.com/MartijnWisse/mirte_navigation) ROS package from GitHub which provides ready-to-use configuration files and SLAM parameter settings.
It was assumed the robot would only navigate in unknown environments without predefined or reoccurring maps. Therefore localization (using AMCL) was disabled in the application.

### Navigation
>
> NAV2

### Manipulation

While the arm on the MIRTE Master can be controlled in joint-space, the implementation relies on task-space (cartesian-space) control over the end effector position. \
The manner in motion planners are typically implemented requires the integration of several complex subsystems like inverse and forward kinematic solvers, trajectory planners and path planners. To accomplish the goal of task space control over the arm, MoveIt 2 {cite:t}`Coleman2014MoveIt` was used.

### Vision
