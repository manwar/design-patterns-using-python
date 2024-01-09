## Factory

In Factory  pattern, we  create  object without exposing the creation
logic to  the client and refer to newly created object using a common
interface.

## IMPLEMENTATION

#### Interface:

**Source**: [Shape.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/Shape.py)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def area(self):
        pass
```

#### Concrete Classes implementing interface `Shape`

**Source**: [Circle.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/Circle.py)
```python
from Shape import Shape

class Circle(Shape):
    def area(self, radius):
        return 3.14 * (radius ** 2)
```

**Source**: [Square.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/Square.py)
```python
from Shape import Shape

class Square(Shape):
    def area(self, side):
        return side * side
```

**Source**: [Rectangle.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/Rectangle.py)
```python
from Shape import Shape

class Rectangle(Shape):
    def area(self, length, width):
        return length * width
```

#### Factory Generator

**Source**: [ShapeFactory.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/ShapeFactory.py)
```python
from Circle import Circle
from Square import Square
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
```

**Source**: [test_factory.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/test_factory.py)
```python
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
```

## DEMO

Show time, with the command `pytest -v`

    test_factory.py::test_circle_area PASSED
    test_factory.py::test_square_area PASSED
    test_factory.py::test_rectangle_area PASSED
