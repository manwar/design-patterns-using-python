## Singleton

This pattern involves a  single  class which is responsible to create
an object while making sure that only single object gets created.This
class provides a way to access  its only object which can be accessed
directly without need to instantiate the object of the class.

## IMPLEMENTATION

**Source**: [Singleton.py](https://github.com/manwar/design-patterns-using-python/blob/master/01-singleton/Singleton.py)
```python
class Singleton:
    __instance = None

    @classmethod
    def instance(cls):
    	if Singleton.__instance == None:
            __instance = super(Singleton, cls).__new__(cls)
    	return __instance
```

**Source**: [SingleObject.py](https://github.com/manwar/design-patterns-using-python/blob/master/01-singleton/SingleObject.py)
```python
from Singleton import Singleton

class SingleObject(Singleton):
    __count = 0
    def counter(self):
    	SingleObject.__count += 1
    	return SingleObject.__count
```

**Source**: [test_singleton.py](https://github.com/manwar/design-patterns-using-python/blob/master/01-singleton/test_singleton.py)
```python
import pytest
from SingleObject import SingleObject

def test_singleton():
    assert SingleObject.instance().counter() == 1
    assert SingleObject.instance().counter() == 2
    assert SingleObject.instance().counter() == 3
    assert SingleObject.instance().counter() == 4
    assert SingleObject.instance().counter() == 5
```

## DEMO

Show time, with the command `pytest -v`

    test_singleton.py::test_singleton PASSED
