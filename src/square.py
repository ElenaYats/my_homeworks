from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides must be greater then zero")
        super().__init__(side_a, side_a)