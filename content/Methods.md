# Experimental Methods

This study follows factorial experimental design, analyzing the interplay between
perception, coverage and system level decision making.

Two independent variables are defined:

- detection method
    * Point cloud clustering
    * 2D Depth projection

- coverage strategy
    * Boustrophedon Coverage
    * Morphology based skeleton Coverage
    * Spanning tree coverage

this results in a total of 16 experimental configurations, however some of these setups are fundamentally incompatible, such as Systematic coverage with a clean as you go approach. The full setup is shown in table x.

## Evaluation Metrics

### Task level metrics
>percentage of electronics, total completion time, failed attempts, distance traveled

### Component level metrics
>detection percision and recall, localization error, coverage percentage.