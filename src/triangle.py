from src.figures import Figure
import math
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides must be greater then zero")
        if not ((side_a + side_b) > side_c and (side_a + side_c) > side_b and (side_b + side_c) > side_a):
            raise ValueError("The sum of two sides must be greater then third side")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c