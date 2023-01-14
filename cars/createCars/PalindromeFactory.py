from abc import ABC
from CarFactory import CarFactory
from batteries import SpindlerBattery
from engines import SternmanEngine
from cars.CarInterface import CarInterface

class PalindromeCreator(CarFactory, ABC):
    def createCar(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        newPalindrome = CarInterface(engine, battery)

        return newPalindrome