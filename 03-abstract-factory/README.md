## Abstract Factory

Abstract Factory patterns  work around a super-factory  which creates
other factories. This factory is also called as factory of factories.
This type of design pattern  comes  under  creational pattern as this
pattern provides one of the best ways to create an object.

In Abstract Factory  pattern an interface is responsible for creating
a factory  of  related  objects  without  explicitly specifying their
classes.  Each  generated  factory  can  give  the objects as per the
Factory pattern.

## IMPLEMENTATION

#### Interface:

**Source**: [Shape.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/Shape.py)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def name(self):
        pass
```

#### Concrete Classes implementing interface `Shape`

**Source**: [Circle.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/Circle.py)
```python
from Shape import Shape

class Circle(Shape):
    def name(self):
        return 'Circle'

class RoundedCircle(Shape):
    def name(self):
        return 'Rounded Circle'
```

**Source**: [Square.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/Square.py)
```python
from Shape import Shape

class Square(Shape):
    def name(self):
        return 'Square'

class RoundedSquare(Shape):
    def name(self):
        return 'Rounded Square'
```

**Source**: [Rectangle.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/Rectangle.py)
```python
from Shape import Shape

class Rectangle(Shape):
    def name(self):
        return 'Rectangle'

class RoundedRectangle(Shape):
    def name(self):
        return 'Rounded Rectangle'
```

#### Abstract Class

**Source**: [AbstractClass.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/AbstractClass.py)
```python
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_shape(self):
        pass
```

#### Concrete Classes implementing interface `Abstractlass`

**Source**: [ShapeFactory.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/Factory.py)
```python
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
```

#### Factory Producer

**Source**: [ShapeFactory.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/Factory.py)
```python
class FactoryProducer:

    @classmethod
    def get_factory(cls, rounded):
        if rounded:
            return RoundedShapeFactory()
        return ShapeFactory()
```

**Source**: [test_abstract_factory.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/test_abstract_factory.py)
```python
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
```

## DEMO

Show time, with the command `pytest -v`

