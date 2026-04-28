# Methodology

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