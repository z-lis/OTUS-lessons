from src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Can not create Circle, radius must be greater than 0')
        super(Circle, self).__init__('Circle')
        self.radius = radius

    def get_area(self):
        return round(math.pi, 2) * self.radius ** 2

    def get_perimeter(self):
        return 2 * round(math.pi, 2) * self.radius
