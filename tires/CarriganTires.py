from abc import ABC
from tires.TireInterface import TireInterface

class CarriganTires(TireInterface, ABC):
    def __init__(self, tireArray):
        self.tireArray = tireArray
    def needs_service(self):
        for value in self.tireArray:
            if value >= 0.9:
                return True
        return False