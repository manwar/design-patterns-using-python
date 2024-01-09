from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_shape(self):
        pass
