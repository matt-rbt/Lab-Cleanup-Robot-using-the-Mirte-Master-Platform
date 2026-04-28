# Theory
Autonomous mobile manipulation requires the integration of navigation, mapping, perception, and localization into a unified system. In this work, these components are orchestrated using a behavior-based control framework.

---

## Navigation
Navigation refers to the process of planning and executing collision-free motion from a start to a goal position. It is typically decomposed into:

* **Global planning**: computing an optimal path on a map.
* **Local planning**: generating feasible velocity commands.

Modern navigation systems use costmaps and search-based planners such as A* or Dijkstra. In Nav2, navigation is modular, allowing different planners and controllers to be interchanged.
Since Local planning can mostly be left to Nav2 for this section only some theory is discussed on how coverage path planning is done in this case.

### Global Planning Methods
Global Path planning includes two major steps. Namely Decomposition and Path planning

---
## Mapping

Mapping is the process of constructing a representation of the environment. In unknown environments, this is often addressed using **Simultaneous Localization and Mapping (SLAM)**.

A common representation is the **occupancy grid**, where each cell encodes the probability of being occupied. Mapping can be expressed probabilistically as:

$$
p(m \mid z_{1:t}, x_{1:t})
$$

where:

* $m$ is the map
* $z_{1:t}$ are sensor measurements
* $x_{1:t}$ are robot poses

Different SLAM approaches (e.g., grid-based vs feature-based) trade off accuracy, computational cost, and robustness.

---

## Localization

Localization estimates the robot’s pose within a known map. A widely used approach is **probabilistic localization**, such as particle filters.

The recursive Bayesian update is given by:

$$
p(x_t \mid z_{1:t}, u_{1:t}) \propto p(z_t \mid x_t), p(x_t \mid u_t, x_{t-1})
$$

where:

* $x_t$ is the robot pose
* $z_t$ is the observation
* $u_t$ is the control input

In practice, methods like Adaptive Monte Carlo Localization (AMCL) are commonly used within Nav2.

---

## Perception

Perception enables the robot to interpret sensor data to detect and classify objects. This includes:

* **Object detection**: identifying candidate objects in the scene
* **Classification**: assigning semantic labels (e.g., electronics vs other)

Libraries such as OpenCV and Open3D are commonly used for image and point cloud processing.

Perception outputs are used by higher-level decision systems to guide actions such as navigation and manipulation.

---

equation example:
$$\oint_C \varphi$$

(schrodinger)=
$$
i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi
$$

We can link to equations using their labels, like equation {numref}`schrodinger` or with more emphasis: {numref}`eq {number} <schrodinger>`. See the [documentation](https://mystmd.org/guide/math) for more options with using formulas. You might be interested in [specific ways of numbering](https://mystmd.org/guide/cross-references#continuous-numbering).