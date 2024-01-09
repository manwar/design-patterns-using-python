from Circle import Circle, RoundedCircle
from Square import Square, RoundedSquare
from Rectangle import Rectangle, RoundedRectangle
from AbstractFactory import AbstractFactory

class ShapeFactory(AbstractFactory):
    _dispatch = {
        'CIRCLE': Circle,
        'SQUARE': Square,
        'RECTANGLE': Rectangle
    }

    @classmethod
    def get_shape(cls, type):
        if type.upper() in cls._dispatch:
            return cls._dispatch[type.upper()]()
        raise ValueError

class RoundedShapeFactory(AbstractFactory):
    _dispatch = {
        'CIRCLE': RoundedCircle,
        'SQUARE': RoundedSquare,
        'RECTANGLE': RoundedRectangle
    }

    @classmethod
    def get_shape(cls, type):
        if type.upper() in cls._dispatch:
            return cls._dispatch[type.upper()]()
        raise ValueError

class FactoryProducer:

    @classmethod
    def get_factory(cls, rounded):
        if rounded:
                return RoundedShapeFactory()
        return ShapeFactory()
