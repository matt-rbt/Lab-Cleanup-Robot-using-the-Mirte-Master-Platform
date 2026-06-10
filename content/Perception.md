# Perception
Perception is responsible for object detection, classification and spatial localization. For this study the object detection and localization approaches were limited to two. A **2D detection and depth projection** approach and 3D segmentation with **point cloud clustering**.
As for classification methods, this study evaluates a classical cv approach, as well as a classification model based approach.

Originally, objects where categorized into:
1. Graspable vs non-graspable
2. Electronics vs non-electronics

However, due to the limitations of the hardware of the standard MIRTE Master package (relatively low-quality camera and limited computing power) the scope got reduced to:

1. Graspable vs non-graspable
2. Colourful vs greyscale 

## Point Cloud-Based Object Localisation

To determine the exact location of graspable objects around the MIRTE Master, the data gathered and transmitted by the camera must be interpreted. One effective method for achieving this is through the use of point clouds. As the name suggests, point clouds are collections of points that represent a three-dimensional space. Depending on how they are generated, points may contain various types of information. However, the most important characteristic of a point is its position, represented by its *x*, *y*, and *z* coordinates.

These coordinates can be used to determine whether a point belongs to a planar surface, such as the floor, a wall, a tabletop, or a table leg. Plane detection is performed using the **Random Sample Consensus (RANSAC)** algorithm. RANSAC randomly selects a subset of points from the point cloud and fits a plane through them. It then evaluates which points in the cloud lie within a predefined distance of the estimated plane, thereby identifying inliers that belong to the same surface ([source](Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography)).

Using this approach, point clouds can be efficiently filtered so that only the relevant parts remain, namely the clusters of points representing small objects on the ground. Subsequently, a clustering algorithm known as **DBSCAN** (*Density-Based Spatial Clustering of Applications with Noise*) is applied. DBSCAN analyses the remaining points and groups them into clusters based on point density, while simultaneously identifying noise and outliers ([source](A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise)).

Once the clusters have been identified, they are converted into bounding boxes. These bounding boxes provide estimates of an object's position, orientation, and dimensions. Finally, the resulting object poses (position and orientation) are published on a ROS 2 topic, allowing any other node in the system to access and use the localisation data.