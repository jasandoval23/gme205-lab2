### 1. Object vs Geometry

Modeling points as objects helped me understand that the data is not just a table of coordinates. Each Point has its own identity, coordinates, and other information, and it can also perform certain actions, such as calculating its distance from another point.

### 2. Responsibility

I learned that it is better to give each part of the program its own responsibility. The Point class handles things related to individual points, such as checking the coordinates and calculating distance. The PointSet class handles the points as a group, such as counting them, finding the bounding box, and filtering them by tag. The runner script is mainly responsible for plotting the points and saving the output files.

### 3. Modeling Insight

Separating the geometry, information, and behavior made the code easier for me to understand. Since each class has a specific purpose, it was easier to see where each part of the spatial logic belonged. Keeping the plotting and file-writing outside the spatial classes also made the code more organized.
