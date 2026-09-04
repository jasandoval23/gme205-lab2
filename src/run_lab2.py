import json
import os
import matplotlib.pyplot as plt

from spatial import PointSet


# Load points
points = PointSet.from_csv("data/points.csv")

# Compute spatial information
bbox = points.bbox()

# Count points by tag
tag_counts = {}

for point in points.points:
    tag = point.tag or "None"
    tag_counts[tag] = tag_counts.get(tag, 0) + 1


# Make output folder
os.makedirs("output", exist_ok=True)


# Create scatter plot
x = [point.lon for point in points.points]
y = [point.lat for point in points.points]

plt.scatter(x, y)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Lab 2 Point Visualization")
plt.savefig("output/lab2_preview.png")
plt.close()


# Create JSON report
report = {
    "total_point_count": points.count(),
    "bounding_box": bbox,
    "counts_per_tag": tag_counts
}

with open("output/lab2_report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("Generated lab2_preview.png")
print("Generated lab2_report.json")