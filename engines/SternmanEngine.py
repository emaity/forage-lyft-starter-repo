from abc import ABC
from engines.EngineInterface import EngineInterface

class SternmanEngine(EngineInterface, ABC):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on
    
    def needs_service(self):
        return self.warning_light_is_on