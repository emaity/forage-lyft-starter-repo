from abc import ABC
from CarFactory import CarFactory
from batteries import NubbinBattery
from engines import WilloughbyEngine
from cars.CarInterface import CarInterface

class RorschachCreator(CarFactory, ABC):
    def createCar(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        newRorschach = CarInterface(engine, battery)

        return newRorschach