from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def createCar():
        pass