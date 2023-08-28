from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError('Can not create Rectangle, sides must be greater than 0')
        super().__init__('Rectangle')
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
