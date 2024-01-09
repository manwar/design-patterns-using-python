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
        'CIRCLE': Circle,
        'SQUARE': Square,
        'RECTANGLE': Rectangle
    }

    @classmethod
    def get_shape(cls, type):
        if type.upper() in cls._dispatch:
            return cls._dispatch[type.upper()]()
        rsises ValueError
```

**Source**: [test_factory.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/test_factory.py)
```python
import pytest
from pytest import approx
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
```

## DEMO

Show time, with the command `pytest -v`

    test_factory.py::test_circle_area PASSED
    test_factory.py::test_square_area PASSED
    test_factory.py::test_rectangle_area PASSED
    test_factory.py::test_mixed_case_shape PASSED
    test_factory.py::test_bad_shape PASSED
