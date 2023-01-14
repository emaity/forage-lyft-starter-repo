from abc import ABC
from CarFactory import CarFactory
from batteries import SpindlerBattery
from engines import WilloughbyEngine
from cars.CarInterface import CarInterface

class GlissadeCreator(CarFactory, ABC):
    def createCar(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        newGlissade = CarInterface(engine, battery)

        return newGlissade