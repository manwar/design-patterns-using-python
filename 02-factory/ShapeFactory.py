from Circle    import Circle
from Square    import Square
from Rectangle import Rectangle

class ShapeFactory:
    _dispatch = {
        'CIRCLE': Circle(),
        'SQUARE': Square(),
        'RECTANGLE': Rectangle()
    }

    def get_shape(self, type):
        if type in self._dispatch:
            return self._dispatch[type]
