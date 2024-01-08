## Singleton
***

This pattern involves a  single  class which is responsible to create
an object while making sure that only single object gets created.This
class provides a way to access  its only object which can be accessed
directly without need to instantiate the object of the class.

## IMPLEMENTATION
***

```python
class Singleton:
    __instance = None

    @classmethod
    def instance(cls):
    	if Singleton.__instance == None:
    		__instance = super(Singleton, cls).__new__(cls)
    	return __instance

class SingleObject:
    __count == 0
    def counter(self):
    	SingleObject.__count += 1
    	return SingleObject.__count

print(SingleObject.instance().counter())  # prints 1
print(SingleObject.instance().counter())  # prints 2
print(SingleObject.instance().counter())  # prints 3
print(SingleObject.instance().counter())  # prints 4
print(SingleObject.instance().counter())  # prints 5
