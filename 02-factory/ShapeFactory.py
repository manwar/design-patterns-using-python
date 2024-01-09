from Circle    import Circle
from Square    import Square
from Rectangle import Rectangle

class ShapeFactory:
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
