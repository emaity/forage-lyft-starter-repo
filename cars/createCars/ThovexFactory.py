from abc import ABC
from CarFactory import CarFactory
from batteries import NubbinBattery
from engines import CapuletEngine
from cars.CarInterface import CarInterface

class ThovexCreator(CarFactory, ABC):
    def createCar(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        newThovex = CarInterface(engine, battery)

        return newThovex