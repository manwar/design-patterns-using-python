from Singleton import Singleton

class SingleObject(Singleton):
    __count = 0
    def counter(self):
        SingleObject.__count += 1
        return SingleObject.__count
