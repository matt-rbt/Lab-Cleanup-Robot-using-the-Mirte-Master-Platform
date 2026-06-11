# Methodology

This study follows a factorial experimental design, analyzing the interplay between perception, coverage, and system-level decision-making.

Two independent variables are defined:

- **Detection method:**
  - Point cloud clustering
  - 2D depth projection

- **Coverage strategy:**
  - Boustrophedon coverage
  - Morphology-based skeleton coverage
  - Spanning tree coverage

This results in a total of 16 experimental configurations. However, some of these setups are fundamentally incompatible, such as systematic coverage with a clean-as-you-go approach.

---

## From Simulation to Real-World Application
\section{Methodology}
\begin{paracol}
    {2}

    This study follows factorial experimental design, analyzing the interplay between perception, coverage and system-level decision making.
    Three independent variables are defined:
    \begin{itemize}
    \item Detection method:
    
    \begin{itemize}
    \item Point cloud clustering
    \item 2D Depth projection
    \end{itemize}

    \item Coverage strategy:

    \begin{itemize}
    \item Morphology based skeleton Coverage
    \item Spanning tree coverage
    \end{itemize}

    \begin{itemize}
    \item Systematic coverage
    \item Clean as-you-go
    \end{itemize}

    This allows for a total of 8 possible configurations to be tested and compared.

    \medskip
    \centerline{\rule{7.8cm}{0.4pt}}
    
    \subsection{From Simulation to Real-World Application}
    For the transition from simulation to real-world testing the codebase needed to be changed. The launch files were changed so that Gazebo did not run and \texttt{use\_sim\_time} parameters were set to \texttt{false}. To reduce the risk of collisions, the inflation radius and the robot radius in NAV2 were increased. Another change was the migration of processing tasks from the OrangePi3B to a laptop connected to the MIRTE. Finally, all the sensors were tested and it was concluded that the depth camera was not positioned correctly, requiring it to be moved to the wrist, which enabled an adjustable position and viewing angle.

    \syncallcounters
    \switchcolumn
    \subsection{Choice of testing environment}

    For testing, an open, medium-sized room was chosen. The room needed to have sufficiently large open spaces for the robot to be able to correctly plan its trajectories for the object detection phase. Due to the use of mecanum wheels and camera based object detection, the room also needed to have a mostly-smooth, flat floor with a uniform colour.
    
    \medskip
    \centerline{\rule{7.8cm}{0.4pt}}
    \subsection{Choice of testing objects}
    
    Due to low video output quality of the included USB camera module, including significant motion blur and difficulties with exposure under different lighting conditions, the success rate of recognition and classification of the electronics was too low. Additionally, most electronics waste had too low of a profile to be recognized by the depth camera. As a result, it was chosen to 3D-print coloured shapes with a textured outer wall for grip, and a custom dataset was created for the object classification model to improve object detection performance.    
\end{paracol}
For the transition from simulation to real-world testing, the codebase needed to be changed. The launch files were modified so that Gazebo was no longer started, and the `use_sim_time` parameters were commented out. To reduce the risk of collisions, the inflation radius and robot radius in NAV2 were increased. Another change was the migration of processing tasks from the OrangePi3B to a laptop connected to the MIRTE.

Finally, all sensors were tested, and it was concluded that the depth camera was not positioned correctly. Therefore, the depth camera was moved from the front of the robot to the gripper, allowing its position and viewing angle to be adjusted.

## Choice of Testing Environment

For testing, an open, medium-sized room was chosen. The room needed to have sufficiently large open spaces for the robot to correctly plan its trajectories during the object detection phase. Due to the use of mecanum wheels and camera-based object detection, the room also needed to have a mostly smooth, flat floor with a uniform color.

---

## Choice of Testing Objects

Due to the low video output quality of the included USB camera module, including significant motion blur and difficulties with exposure under different lighting conditions, the success rate of recognition and classification of electronic waste was too low. Additionally, most electronic waste had too low a profile to be recognized by the depth camera.

As a result, it was decided to 3D-print colored shapes with a textured outer wall to improve gripping performance. A custom dataset was also created for the object classification model to improve object detection performance.