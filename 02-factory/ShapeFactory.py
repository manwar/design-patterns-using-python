from Shape import Shape
from Circle import Circle
from Square import Square
from Rectangle import Rectangle

class ShapeFactory(Shape):
    _dispatch = {
        'CIRCLE': Circle(),
        'SQUARE': Square(),
        'RECTANGLE': Rectangle()
    }

    def get_shape(type):
        if type in ShapeFactory._dispatch:
            return ShapeFactory._dispatch[type]
            #super(Shape, cls).__new__(cls)
