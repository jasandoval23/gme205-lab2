from src.spatial import Point, PointSet


def test_point():
    p = Point("A", 121.0, 14.6)
    assert p.to_tuple() == (121.0, 14.6)


def test_pointset():
    points = PointSet.from_csv("data/points.csv")
    assert points.count() == 9
    assert len(points.filter_by_tag("poi").points) == 3
    