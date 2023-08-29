from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError('Can not create Triangle, sides must be greater than 0')
        elif side_c > (side_a + side_b) or side_a > (side_b + side_c) or side_b > (side_a + side_c):
            raise ValueError('Can not create Triangle, the length of any side of a triangle cannot be greater than '
                             'the sum of the lengths of the other two sides')

        super().__init__('Triangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        half_perimeter = self.get_perimeter()/2
        return (half_perimeter * (half_perimeter - self.side_a) * (half_perimeter - self.side_b)
                * (half_perimeter - self.side_c)) ** 0.5

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
