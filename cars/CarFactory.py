from abc import ABC
from cars.CarInterface import CarInterface
from engines.CapuletEngine import CapuletEngine
from engines.WilloughbyEngine import WilloughbyEngine
from engines.SternmanEngine import SternmanEngine
from batteries.SpindlerBattery import SpindlerBattery
from batteries.NubbinBattery import NubbinBattery

class CarFactory(ABC):
    def createCalliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        newCalliope = CarInterface(engine, battery)

        return newCalliope

    def createGlissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        newGlissade = CarInterface(engine, battery)

        return newGlissade

    def createPalindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        newPalindrome = CarInterface(engine, battery)

        return newPalindrome

    def createRorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        newRorschach = CarInterface(engine, battery)

        return newRorschach

    def createThovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        newThovex = CarInterface(engine, battery)

        return newThovex