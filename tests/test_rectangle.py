from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle
import pytest

@pytest.mark.parametrize("side_a, side_b, area",
                         [(3, 5, 15),
                          (3.5, 5.5, 19.25)])
@pytest.mark.smoke
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(3, 5)
    assert r.area == 15, f"Expected area should be {3 * 5}"

@pytest.mark.parametrize("side_a, side_b, perimeter",
                         [(3, 5, 16),
                          (3.5, 5.5, 19.25)])
@pytest.mark.smoke
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(3, 5)
    assert r.perimeter == 16, f"Expected perimeter should be {(3 + 5)*2}"

@pytest.mark.parametrize("side_a, side_b",
                         [(0, 5),
                          (1, 0),
                          (-5, 10),
                          (10, -5)])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError, match="Rectangle sides must be greater then zero"):
        Rectangle(side_a, side_b)

@pytest.mark.parametrize("rectangle_sides, circle_radius", [
    ((10, 5), 6),
    ((5.5, 7.5), 9.5)
])
@pytest.mark.smoke
def test_rectangle_circle_add_area_positive(rectangle_sides, circle_radius):
    rectangle = Rectangle(*rectangle_sides)
    circle = Circle(circle_radius)
    expected_area = rectangle.area + circle.area
    assert rectangle.add_area(circle) == expected_area, f"Wrong value circle + rectangle"

@pytest.mark.parametrize("rectangle_sides, square_side", [
    ((10, 5), 6),
    ((5.5, 7.5), 9.5)
])
def test_rectangle_square_add_area_positive(rectangle_sides, square_side):
    rectangle = Rectangle(*rectangle_sides)
    square = Square(square_side)
    expected_area = rectangle.area + square.area
    assert rectangle.add_area(square) == expected_area, f"Wrong value square + rectangle"

@pytest.mark.parametrize("rectangle_sides, triangle_sides", [
    ((10, 5), (3, 5, 4)),
    ((5.5, 7.5), (7.0, 8.0, 6.0))
])
def test_rectangle_triangle_add_area_positive(rectangle_sides, triangle_sides):
    rectangle = Rectangle(*rectangle_sides)
    triangle = Triangle(*triangle_sides)
    expected_area = rectangle.area + triangle.area
    assert rectangle.add_area(triangle) == expected_area, f"Wrong value triangle + rectangle"

@pytest.mark.parametrize("rectangle1_sides, rectangle2_sides", [
    ((10, 5), (7, 6)),
    ((5.5, 7.5), (2.6, 9.5))
])
def test_rectangle_rectangle_add_area_positive(rectangle1_sides, rectangle2_sides):
    rectangle1 = Rectangle(*rectangle1_sides)
    rectangle2 = Rectangle(*rectangle2_sides)
    expected_area = rectangle1.area + rectangle2.area
    assert rectangle1.add_area(rectangle2) == expected_area, f"Wrong value rectangle + rectangle"