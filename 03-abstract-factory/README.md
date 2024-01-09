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
    def area(self):
        pass
```

#### Concrete Classes implementing interface `Shape`

**Source**: [Circle.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/Circle.py)
```python
from Shape import Shape

class Circle(Shape):
    def area(self, radius):
        return 3.14 * (radius ** 2)
```

**Source**: [Square.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/Square.py)
```python
from Shape import Shape

class Square(Shape):
    def area(self, side):
        return side * side
```

**Source**: [Rectangle.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/Rectangle.py)
```python
from Shape import Shape

class Rectangle(Shape):
    def area(self, length, width):
        return length * width
```

#### Abstract Class

**Source**: [AbstractClass.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/AbstractClass.py)
```python
```

#### Concrete Classes implementing interface `Abstractlass`

**Source**: [ShapeFactory.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/ShapeFactory.py)
```python
```

#### Factory Generator

**Source**: [FactoryProducer.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/FactoryProducer.py)
```python
```

**Source**: [test_abstract_factory.py](https://github.com/manwar/design-patterns-using-python/blob/master/03-abstract-factory/test_abstract_factory.py)
```python
import pytest
from pytest import approx
```

## DEMO

Show time, with the command `pytest -v`

