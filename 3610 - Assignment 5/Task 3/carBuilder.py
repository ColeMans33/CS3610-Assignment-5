from abc import ABC, abstractmethod
from car import Car
from builder import Builder


class CarBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def setSeats(self, number: int):
        self.car.seats = number

    def setEngine(self, engine: str):
        self.car.engine = engine

    def setTripComputer(self):
        self.car.tripComputer = True

    def setGPS(self):
        self.car.gps = True

    def getResult(self) -> Car:
        return self.car
