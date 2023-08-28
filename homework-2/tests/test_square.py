import pytest
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize('side_a, area, perimeter',
                         [
                             (4, 16, 16),
                             (10, 100, 40)
                         ])
def test_square(side_a, area, perimeter):
    square = Square(side_a)
    assert square.name == "Square"
    assert square.get_area() == area
    assert square.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, area, perimeter',
                         [
                             (-7, 49, -28),
                             (0, 0, 0)
                         ])
def test_square_negative(side_a, area, perimeter):
    with pytest.raises(ValueError):
        Square(side_a)


def test_square_area_sums():
    square = Square(67)
    other_figure = Triangle(3, 4, 5)
    assert square.add_area(other_figure) == 4489 + 6


def test_square_area_sums_negative():
    square = Square(6)
    other_figure = 'Some text'
    with pytest.raises(ValueError):
        square.add_area(other_figure)
