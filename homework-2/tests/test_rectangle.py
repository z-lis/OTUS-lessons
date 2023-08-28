import pytest
from src.Rectangle import Rectangle
from src.Square import Square


@pytest.mark.parametrize('side_a, side_b, area, perimeter',
                         [
                             (4, 5, 20, 18),
                             (10, 20, 200, 60)
                         ])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == "Rectangle"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, area, perimeter',
                         [
                             (-7, 1, -7, 16),
                             (0, 13, 0, 26)
                         ])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_rectangle_area_sums():
    rectangle = Rectangle(5, 9)
    other_figure = Square(11)
    assert rectangle.add_area(other_figure) == 45 + 121


def test_rectangle_area_sums_negative():
    rectangle = Rectangle(4, 6)
    other_figure = 'Some text'
    with pytest.raises(ValueError):
        rectangle.add_area(other_figure)
