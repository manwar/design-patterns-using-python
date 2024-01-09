import pytest
from pytest import approx
from ShapeFactory import ShapeFactory

@pytest.fixture()
def shape_factory():
    return ShapeFactory()

def test_circle_area(shape_factory):
    circle = shape_factory.get_shape("CIRCLE")
    assert approx(circle.area(10)) == 314

def test_square_area(shape_factory):
    square = shape_factory.get_shape("SQUARE")
    assert approx(square.area(3)) == 9

def test_rectangle_area(shape_factory):
    rectangle = shape_factory.get_shape("RECTANGLE")
    assert approx(rectangle.area(2, 4)) == 8
