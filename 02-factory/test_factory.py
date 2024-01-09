import pytest
from pytest import approx
from ShapeFactory import ShapeFactory

def test_circle_area():
    circle = ShapeFactory.get_shape("CIRCLE")
    assert approx(circle.area(10)) == 314

def test_square_area():
    square = ShapeFactory.get_shape("SQUARE")
    assert approx(square.area(3)) == 9

def test_rectangle_area():
    rectangle = ShapeFactory.get_shape("RECTANGLE")
    assert approx(rectangle.area(2, 4)) == 8
