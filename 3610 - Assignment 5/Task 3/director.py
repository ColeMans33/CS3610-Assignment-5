from abc import ABC, abstractmethod
from builder import Builder
import random




class Director:
  def makeSUV(self, builder: Builder):
    builder.reset()
    builder.setSeats(4)
    builder.setEngine("SUV engine")

  def makeSportsCar(self, builder: Builder):
    builder.reset()
    builder.setSeats(2)
    builder.setEngine("Sports engine")
    builder.setGPS()

  def makeRandomCar(self, builder: Builder):
    builder.reset
    builder.setSeats(random.randint(1,8))
    builder.setEngine("Caravan")
    if(random.randint(0,1) == 1):
      builder.setTripComputer()
      builder.setGPS()
    else:
      None
