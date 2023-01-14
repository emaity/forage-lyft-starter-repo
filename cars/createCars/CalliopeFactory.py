from abc import ABC
from CarFactory import CarFactory
from batteries import SpindlerBattery
from engines import CapuletEngine
from cars.CarInterface import CarInterface

class CalliopeCreator(CarFactory, ABC):
    def createCar(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        newCalliope = CarInterface(engine, battery)

        return newCalliope
