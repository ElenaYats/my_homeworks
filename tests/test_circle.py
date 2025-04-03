from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle
import pytest

@pytest.mark.parametrize("circle_radius, area",
                         [((5), 78.5),
                         ((5.5),95)
                         ])
@pytest.mark.smoke
def test_circle_area_positive(circle_radius, area):
    circle = Circle(circle_radius)
    assert round(circle.area, 1) == area, f"Expected area should be {area}"

@pytest.mark.parametrize("circle_radius, perimeter",
                         [((5), 78.5),
                         ((5.5),95)
                         ])
@pytest.mark.smoke
def test_circle_perimeter_positive(circle_radius, perimeter):
    circle = Circle(circle_radius)
    assert round(circle.area, 1) == perimeter, f"Expected area should be {perimeter}"

@pytest.mark.parametrize("radius",
                         [(0),
                          (-1)])
def test_circle_negative(radius):
    with pytest.raises(ValueError, match="The radius of the circle must be greater than zero"):
        Circle(radius)

@pytest.mark.parametrize("rectangle_sides, circle_radius", [
    ((10, 5), 6),
    ((5.5, 7.5), 9.5)
])
@pytest.mark.smoke
def test_rectangle_circle_add_area_positive(rectangle_sides, circle_radius):
    rectangle = Rectangle(*rectangle_sides)
    circle = Circle(circle_radius)
    expected_area = rectangle.area + circle.area
    assert circle.add_area(rectangle) == expected_area, f"Wrong value circle + rectangle"

@pytest.mark.parametrize("square_side, circle_radius", [
    ((5), 6),
    ((7.5), 9.5)
])
def test_square_circle_add_area_positive(square_side, circle_radius):
    square = Square(square_side)
    circle = Circle(circle_radius)
    expected_area = square.area + circle.area
    assert circle.add_area(square) == expected_area, f"Wrong value circle + square"

@pytest.mark.parametrize("circle1_radius, circle2_radius", [
    (5, 6),
    (7.5, 9.5)])
def test_circle_circle_add_area_positive(circle1_radius, circle2_radius):
    circle1 = Circle(circle1_radius)
    circle2 = Circle(circle2_radius)
    expected_area = circle1.area + circle2.area
    assert circle1.add_area(circle2) == expected_area, f"Wrong value circle + circle"

@pytest.mark.parametrize("triangle_sides, circle_radius", [
    ((7, 5, 6), 6),
    ((5.5, 7.5, 6.5), 9.5)
])
def test_triangle_circle_add_area_positive(triangle_sides, circle_radius):
    triangle = Triangle(*triangle_sides)
    circle = Circle(circle_radius)
    expected_area = triangle.area + circle.area
    assert circle.add_area(triangle) == expected_area, f"Wrong value circle + triangle"

