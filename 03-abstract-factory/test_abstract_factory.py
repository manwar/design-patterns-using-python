import pytest
from pytest import raises
from Factory import FactoryProducer

shape_factory = FactoryProducer.get_factory(False)
rounded_shape_factory = FactoryProducer.get_factory(True)

def test_shape_name():
    shapes = {"CIRCLE":"Circle","SQUARE":"Square","RECTANGLE":"Rectangle"}
    for type in shapes:
        assert shape_factory.get_shape(type).name() == shapes[type]

def test_rounded_shape_name():
    shapes = {"CIRCLE":"Rounded Circle","SQUARE":"Rounded Square","RECTANGLE":"Rounded Rectangle"}
    for type in shapes:
        assert rounded_shape_factory.get_shape(type).name() == shapes[type]
