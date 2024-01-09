## Factory

In Factory  pattern, we  create  object without exposing the creation
logic to  the client and refer to newly created object using a common
interface.

## IMPLEMENTATION

#### Interface:

**Source**: [Shape.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/Shape.py)
```python
```

#### Concrete Classes implementing interface `Shape`

**Source**: [Circle.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/Circle.py)
```python
```

**Source**: [Square.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/Square.py)
```python
```

**Source**: [Rectangle.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/Rectangle.py)
```python
```

#### Factory Generator

**Source**: [ShapeFactory.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/ShapeFactory.py)
```python
```

**Source**: [test_factory.py](https://github.com/manwar/design-patterns-using-python/blob/master/02-factory/test_factory.py)
```python
```

## DEMO

Show time, with the command `pytest -v`

    test_factory.py::test_factory PASSED
