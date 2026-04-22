# Methodology

## System Overview
The system essentially consists of a mobile manipulator (Mirte Master) tasked with
autonomously exploring an indoor environment (the robotics lab), identifying objects, distinguishing between electronics and other objects, and sorting these objects accordingly.

the pipeline integrates three main components: **perception**, **coverage planning** and **high-level task strategy**.

### Perception
Perception is responsible for object detection, classification and spatial localization. For this study we limited the object detection and localization approaches to two. A **2D detection and depth projection** approach, and 3D segmentation with **point cloud clustering**.
As for classification methods, this study evaluates a classical cv approach, aswell as a classification model based approach.

objects are categorized into:
1. Graspable vs non-graspable
2. Electronics vs non-electronics

>iets meer over classification.

### Coverage Strategy
Coverage planning refers to how the robot explores the mapped environment to look for graspable objects.
Two coverage strategies are implemented:
- **Systematic coverage:** The environment is traversed using a structured pattern like a  boustrophedon pattern to ensure complete coverage.
- **Reactive coverage**: The robot dynamically traverses and selects exploration targets based on frontier regions or detected objects, prioritizing areas of high information gain.
>iets meer over coverage planning.

### System level strategy
The system level strategy determines when and how the objects are retrieved.
Two high level behaviors are evaluated:
- Clean as you go: The robot attempts to grasp objects upon detection without mapping the environment fully first
- Map and optimize: The robot first explores and maps the environment and stores detected objects. Only after this stage does the robot collect objects based on a calculated plan.
>iets meer over system strategy.

## Experimental design
This study follows factorial experimental design, analyzing the interplay between
perception, coverage and system level decision making.

Three independent variables are defined:

- perception quality
    * Classical cv based classification
    * Model based classification

- detection method
    * point cloud clustering
    * depth projection

- coverage strategy
    * Systematic Coverage following a predefined path
    * Reactive Coverage by acting in real time

- System-level strategy
    * Clean-as-you-go
    * Map-then-optimize

this results in a total of 16 experimental configurations, however some of these setups are fundamentally incompatible, such as Systematic coverage with a clean as you go approach. The full setup is shown in table x.

## Evaluation Metrics

### Task level metrics
>percentage of electronics, total completion time, failed attempts, distance traveled
### Component level metrics
>detection percision and recall, localization error, coverage percentage.