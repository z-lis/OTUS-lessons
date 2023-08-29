from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.get_area() + other_figure.get_area()
        raise ValueError(f'Object {other_figure} is not Figure')
