from abc import ABC, abstractmethod
from manual import Manual
from builder import Builder


class CarManualBuilder(Builder):
  def __init__(self):
    self.reset()

  def reset(self):
    self.manual = Manual()

  def setSeats(self, number: int):
    self.manual.seats = number

  def setEngine(self, engine: str):
    self.manual.engine = engine

  def setTripComputer(self):
    self.manual.tripComputer = True

  def setGPS(self):
    self.manual.gps = True

  def getResult(self) -> Manual:
    return self.manual