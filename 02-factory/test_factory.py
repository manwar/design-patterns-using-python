import pytest
from pytest import approx, raises
from ShapeFactory import ShapeFactory

def test_circle_area():
    assert approx(ShapeFactory.get_shape("CIRCLE").area(10)) == 314

def test_square_area():
    assert approx(ShapeFactory.get_shape("SQUARE").area(3)) == 9

def test_rectangle_area():
    assert approx(ShapeFactory.get_shape("RECTANGLE").area(2, 4)) == 8

def test_mixed_case_shape():
    assert approx(ShapeFactory.get_shape("SqUaRe").area(3)) == 9

def test_bad_shape():
    with raises(ValueError):
        ShapeFactory.get_shape("Bob")
