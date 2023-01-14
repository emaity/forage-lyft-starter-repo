from abc import ABC
from Serviceable import Serviceable

class CarInterface(Serviceable, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    def needs_service(self):
        return self.engine.needs_service() and self.battery.needs_service()