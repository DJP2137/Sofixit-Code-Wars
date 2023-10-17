# Sofixit-Code-Wars
A simple implementation using Python NumPy, and optionally openCV, to display the problem and its solution.
## How it works?
The program accepts heights of each wall in order as a list of integers. It then proceeds to go bottom-up, from 1 to the maximum height of all walls. On each level it finds the index of each wall that is at least as tall as current level. All units between the leftmost and rightmost wall, that are not walls themselves, are able to hold liquid without spilling. The length of the list containing all of their indices is then added to the total amount of units filled.
## OpenCV
Alternatively, one can use the function `materialVisualised`, which, using openCV, draws the scene (background, walls, liquid), and optionally displays a simple animation of filling viable spaces. It is naturally less efficient, but more neat if I do say so myself.

![There should be a cool gif here :/](animated.gif)