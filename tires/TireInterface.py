from abc import ABC, abstractmethod

class TireInterface(ABC):
    @abstractmethod
    def needs_service(self):
        pass