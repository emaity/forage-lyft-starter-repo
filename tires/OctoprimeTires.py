from abc import ABC
from tires.TireInterface import TireInterface

class OctoprimeTires(TireInterface, ABC):
    def __init__(self, tireArray):
        self.tireArray = tireArray
    def needs_service(self):
        sum = 0
        for value in self.tireArray:
            sum += value
        if sum >= 3:
            return True
        return False