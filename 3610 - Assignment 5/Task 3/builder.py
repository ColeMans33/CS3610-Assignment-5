from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setSeats(self, number: int):
        pass

    @abstractmethod
    def setEngine(self, engine: str):
        pass

    @abstractmethod
    def setTripComputer():
        pass

    @abstractmethod
    def setGPS():
        pass
