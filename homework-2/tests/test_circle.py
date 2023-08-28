import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle


@pytest.mark.parametrize('radius, area, perimeter',
                         [
                             (4, 50.24, 25.12),
                             (11, 379.94, 69.08)
                         ])
def test_circle(radius, area, perimeter):
    circle = Circle(radius)
    assert circle.name == "Circle"
    assert circle.get_area() == area
    assert circle.get_perimeter() == perimeter


@pytest.mark.parametrize('radius, area, perimeter',
                         [
                             (-16, 472, -88),
                             (0, 0, 0)
                         ])
def test_circle_negative(radius, area, perimeter):
    with pytest.raises(ValueError):
        Circle(radius)


def test_circle_area_sums():
    circle = Circle(13)
    other_figure = Rectangle(17, 32)
    assert circle.add_area(other_figure) == 530.66 + 544


def test_circle_area_sums_negative():
    circle = Circle(5)
    other_figure = 'Some text'
    with pytest.raises(ValueError):
        circle.add_area(other_figure)
