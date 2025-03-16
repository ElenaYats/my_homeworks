from figure import Figure
class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Rectangle sides must be greater then zero")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b
    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    def add_area(self, other_figure):
        return self.area + other_figure.area

