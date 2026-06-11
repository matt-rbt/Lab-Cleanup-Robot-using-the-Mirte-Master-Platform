# Methodology

This study follows a factorial experimental design, analyzing the interplay between perception, coverage, and system-level decision-making.

Three independent variables are defined:

- **Detection Method:**
  - Point cloud clustering
  - 2D depth projection

- **Coverage Strategy:**
  - Morphology-based skeleton coverage
  - Spanning tree coverage

- **System-level Decision-making:**
  - Systematic coverage
  - Clean as-you-go

This results in a total of 8 configurations to be tested and compared.

## From Simulation to Real-World Application

For the transition from simulation to real-world testing, the codebase needed to be changed. The launch files were changed so that Gazebo was no longer used and `use_sim_time` parameters were set to `false`. To reduce the risk of collisions, the inflation radius and the robot radius in the Nav2 parameters were increased. Another change was the migration of processing tasks from the OrangePi 3B to a laptop connected to the MIRTE. Finally, all the sensors were tested and it was concluded that the depth camera was not positioned correctly and thus its position changed from the front of the robot to the gripper, allowing its position and viewing angle to be adjusted.

##  Choice of Testing Environment

For testing, an open, medium-sized room was chosen. The room needed to have sufficiently large open spaces for the robot to be able to correctly plan its trajectories for the object detection phase. Due to the use of mecanum wheels and camera based object detection, the room also needed to have a mostly-smooth, flat floor with a uniform colour.

##  Choice of Testing Objects
Due to low video output quality of the included USB camera module, including significant motion blur and difficulties with exposure under different lighting conditions, the success rate of recognition and classification of the electronics was too low. Additionally, most electronics waste had too low of a profile to be recognised by the depth camera. As a result, it was chosen to 3D-print coloured shapes with a textured outer wall for grip. A custom dataset was created for the object classification model to improve object detection performance.



  

<!-- ### Task-Level Metrics

>percentage of electronics, total completion time, failed attempts, distance traveled

  

### Component-Level Metrics

>detection percision and recall, localization error, coverage percentage. -->