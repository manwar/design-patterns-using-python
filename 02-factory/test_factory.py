import pytest
from pytest import approx
from ShapeFactory import ShapeFactory

def test_circle_area():
    assert approx(ShapeFactory.get_shape("CIRCLE").area(10)) == 314

def test_square_area():
    assert approx(ShapeFactory.get_shape("SQUARE").area(3)) == 9

def test_rectangle_area():
    assert approx(ShapeFactory.get_shape("RECTANGLE").area(2, 4)) == 8
