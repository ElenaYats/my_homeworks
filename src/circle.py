from figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("The radius of the circle must be greater than zero")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def add_area(self, other_figure):
        return self.area + other_figure.area