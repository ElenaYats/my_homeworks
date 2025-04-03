from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle
import pytest

@pytest.mark.parametrize("side_a, area",
                         [(3, 9),
                          (3.5, 12.25)])
@pytest.mark.smoke
def test_square_area_positive(side_a, area):
    s = Square(side_a)
    assert s.area == area, f"Expected area should be {side_a * side_a}"

@pytest.mark.parametrize("side_a, perimeter",
                         [(3, 12),
                          (3.5, 14)])
@pytest.mark.smoke
def test_square_perimeter_positive(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter, f"Expected perimeter should be {(side_a + side_a)*2}"

@pytest.mark.parametrize("side_a",
                         [(0),
                          (-1)])
def test_square_negative(side_a):
    with pytest.raises(ValueError, match="Square sides must be greater then zero"):
        Square(side_a)

@pytest.mark.parametrize("square1_side, square2_side", [
    ((5), (6)),
    ((5.5), (9.5))
])
@pytest.mark.smoke
def test_square_square_add_area_positive(square1_side, square2_side):
    square1 = Square(square1_side)
    square2 = Square(square2_side)
    expected_area = square1.area + square2.area
    assert square1.add_area(square2) == expected_area, f"Wrong value square + square"

@pytest.mark.parametrize("rectangle_sides, square_side", [
    ((10, 5), 6),
    ((5.5, 7.5), 9.5)
])
def test_rectangle_square_add_area_positive(rectangle_sides, square_side):
    rectangle = Rectangle(*rectangle_sides)
    square = Square(square_side)
    expected_area = rectangle.area + square.area
    assert square.add_area(rectangle) == expected_area, f"Wrong value rectangle + square"

@pytest.mark.parametrize("square_side, triangle_sides", [
    ((5), (3, 5, 4)),
    ((7.5), (7.0, 8.0, 6.0))
])
def test_square_triangle_add_area_positive(square_side, triangle_sides):
    square = Square(square_side)
    triangle = Triangle(*triangle_sides)
    expected_area = square.area + triangle.area
    assert square.add_area(triangle) == expected_area, f"Wrong value triangle + square"

@pytest.mark.parametrize("square_side, circle_radius", [
    ((5), 6),
    ((7.5), 9.5)
])
def test_square_circle_add_area_positive(square_side, circle_radius):
    square = Square(square_side)
    circle = Circle(circle_radius)
    expected_area = square.area + circle.area
    assert square.add_area(circle) == expected_area, f"Wrong value circle + square"
