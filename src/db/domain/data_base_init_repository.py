from abc import ABC,abstractmethod

class DataBaseInitRepository(ABC):
    @abstractmethod
    def initialize():
        ...