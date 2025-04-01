from src.rectangle import Rectangle
from src.figures import Figure
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle
import pytest

@pytest.mark.parametrize("triangle_sides, area",
                         [((5, 5, 6), 12),
                        ((2.5, 3.5, 4.0), 4.3)])
@pytest.mark.smoke
def test_triangle_area_positive(triangle_sides, area):
    triangle = Triangle(*triangle_sides)
    assert round(triangle.area, 1) == area, f"Expected area should be {area}"

@pytest.mark.parametrize("triangle_sides, perimeter",
                         [((5, 5, 6), 16),
                        ((2.5, 3.5, 4.0), 10)])
@pytest.mark.smoke
def test_triangle_perimeter_positive(triangle_sides, perimeter):
    triangle = Triangle(*triangle_sides)
    assert round(triangle.perimeter, 1) == perimeter, f"Expected area should be {perimeter}"

@pytest.mark.parametrize("side_a, side_b, side_c",
                         [(0, 2, 3),
                          (-1, 4, 5),
                          (2, 0, 5),
                          (2, 3, 0),
                          (4, 5, -1),
                          (4, -1, 5)])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError, match="Triangle sides must be greater then zero"):
        Triangle(side_a, side_b, side_c)

@pytest.mark.parametrize("side_a, side_b, side_c",
                         [(6, 2, 3),
                          (4, 10, 3),
                          (7, 3, 15),
                          (5.5, 4.5, 10.5)])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError, match="The sum of two sides must be greater then third side"):
        Triangle(side_a, side_b, side_c)

@pytest.mark.parametrize("triangle1_sides, triangle2_sides", [
    ((5, 6, 7),
    (5.5, 9.5, 10.5))
])
@pytest.mark.smoke
def test_triangle_triangle_add_area_positive(triangle1_sides, triangle2_sides):
    triangle1 = Triangle(*triangle1_sides)
    triangle2 = Triangle(*triangle2_sides)
    expected_area = triangle1.area + triangle2.area
    assert Figure.add_area(triangle1, triangle2) == expected_area, f"Wrong value triangle + triangle"

@pytest.mark.parametrize("rectangle_sides, triangle_sides", [
    ((10, 5), (3, 5, 4)),
    ((5.5, 7.5), (7.0, 8.0, 6.0))
])
def test_rectangle_triangle_add_area_positive(rectangle_sides, triangle_sides):
    rectangle = Rectangle(*rectangle_sides)
    triangle = Triangle(*triangle_sides)
    expected_area = rectangle.area + triangle.area
    assert Figure.add_area(rectangle, triangle) == expected_area, f"Wrong value triangle + rectangle"

@pytest.mark.parametrize("square_side, triangle_sides", [
    ((5), (3, 5, 4)),
    ((7.5), (7.0, 8.0, 6.0))
])
def test_square_triangle_add_area_positive(square_side, triangle_sides):
    square = Square(square_side)
    triangle = Triangle(*triangle_sides)
    expected_area = square.area + triangle.area
    assert Figure.add_area(square, triangle) == expected_area, f"Wrong value triangle + square"

@pytest.mark.parametrize("triangle_sides, circle_radius", [
    ((7, 5, 6), 6),
    ((5.5, 7.5, 6.5), 9.5)
])
def test_triangle_circle_add_area_positive(triangle_sides, circle_radius):
    triangle = Triangle(*triangle_sides)
    circle = Circle(circle_radius)
    expected_area = triangle.area + circle.area
    assert Figure.add_area(triangle, circle) == expected_area, f"Wrong value circle + triangle"