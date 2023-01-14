from abc import ABC
from BatteryInterface import BatteryInterface

class SpindlerBattery(BatteryInterface, ABC):
    def __init__(self, last_service_date, current_date):
        self.years_to_replace = 2
        self.service_threshold_date = last_service_date.replace(year=last_service_date.year + self.years_to_replace)
        self.current_date = current_date
    
    def needs_service(self):
        return self.service_threshold_date < self.current_date