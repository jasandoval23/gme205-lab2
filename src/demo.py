from spatial import Point, PointSet

p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)
print(p.to_tuple())

#q = Point("X", 121.1, 14.1)
#print(q.id, q.lon, q.lat)

q = Point("X", 121.1, 14.1)
print(q.id, q.lon, q.lat)

# Test distance_to()
distance = p.distance_to(q)
print(f"Distance from {p.id} to {q.id}: {distance:.2f} meters")

# Test from_row()
row = {
    "id": "B",
    "lon": 121.05,
    "lat": 14.65,
    "name": "Sample Place",
    "tag": "poi"
}

r = Point.from_row(row)
print(r.id, r.lon, r.lat, r.name, r.tag)

# Test is_poi()
print(f"Is {r.id} a POI? {r.is_poi()}")

#Pointset test
p1 = Point("A", 121.0, 14.6)
p2 = Point("B", 121.1, 14.7)

my_set = PointSet([p1, p2])

print(my_set.points)

#PointSet
points = PointSet.from_csv("data/points.csv")

print("Point count:", points.count())

#Test bbox
print("Bounding box:", points.bbox())

#Test filter
poi_points = points.filter_by_tag("poi")

print("POI count:", poi_points.count())