# Perception
Perception is responsible for object detection, classification and spatial localization. For this study we limited the object detection and localization approaches to two. A **2D detection and depth projection** approach, and 3D segmentation with **point cloud clustering**.
As for classification methods, this study evaluates a classical cv approach, aswell as a classification model based approach......

Originally, objects where categorized into:
1. Graspable vs non-graspable
2. Electronics vs non-electronics

However, due to the limitations of the hardware of the standard MIRTE Master package (low quality camera and low computing power) we reduced our scope to:

1. Graspable vs non-graspable
2. Colourful vs greyscale 

