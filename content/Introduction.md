---
abstract: |
---
In laboratories, items of many kinds may fall onto the floor. While implementations to clean such floors - like robotic vacuum cleaners - already exist, they don't work with trash-separation mechanics and end up disposing of all waste into the same bin. Yet, in laboratories, one may one specific dropped items to be returned and reused, such as electronic components. This project aims to use the open-source MIRTE Master robotic platform to combine both cleaning and reusing, by implementing a sorting system. Using a 4-DOF robotic arm with gripping end-effector, a 2-sided bin, an RGB-D camera, MoveIt! 2 for manipulation and Nav2 for navigation, all built on top of the MIRTE Master platform, a robotic automatically detecting an sorting robot has been realised. During this research, methods for path planning and object detection have been tested, compared and implemented with the goal of making the robot as accurate as possible while maintaining operational velocity.

% Het einde bevat nog geen resultaten, die moeten er wel nog in zodra we die hebben!!

# Introduction


**cite from bib-file**
- `{cite:t}`jupyter2025`` resulting in {cite:t}`jupyter2025`
- `{cite:p}`jupyter2025`` resulting in {cite:p}`jupyter2025`


## Related Works
Jupyter Book has been rebuilt with the intend to export content in multiple output formats including HTML, PDF and docx. {numref}`Figure {number} <fig-diagram>` provides this idea.

```{figure} figures/diagram.*
:label: fig-diagram
:alt: Some figure

The myst engine allows Jupyter Notebook, markdown and even tex files to be converted to multiple output formats.
```

As exporting to different formats is possible, it is not always desired. Some content should only be visible in the HTML version, and some content only need to be included in the PDF version. You can use blocks like `+++{"no-pdf":true}` to enable this, as shown below where the figure is seen in the HTML version but not in the PDF version.

+++{"no-pdf":true}
```{figure} figures/delft.*
:label: fig-delft
:alt: picture of the TUD

A figure that is in the website but not in the PDF version.
```

## Contribution
+++