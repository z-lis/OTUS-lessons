import pytest
from src.triangle import Triangle
from src.circle import Circle


@pytest.mark.parametrize('side_a, side_b, side_c, area, perimeter',
                         [
                             (3, 4, 5, 6, 12),
                             (10, 10, 12, 48, 32)
                         ])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    square = Triangle(side_a, side_b, side_c)
    assert square.name == "Triangle"
    assert square.get_area() == area
    assert square.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, side_c, area, perimeter',
                         [
                             (-7, 18, -28, 84, -17),
                             (0, 0, 0, 0, 0),
                             (10, 10, 32, 90, 52)
                         ])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_triangle_area_sums():
    triangle = Triangle(3, 4, 5)
    other_figure = Circle(7)
    assert triangle.add_area(other_figure) == 6 + 153.86


def test_triangle_area_sums_negative():
    triangle = Triangle(100, 100, 120)
    other_figure = 'Some text'
    with pytest.raises(ValueError):
        triangle.add_area(other_figure)
