from abc import ABC, abstractmethod
from carBuilder import *
from carManualBuilder import *
from director import *


director = Director()
builder = CarBuilder()
director.makeSportsCar(builder)
car = builder.getResult()
print(car)

manualBuilder = CarManualBuilder()
director.makeSUV(manualBuilder)
manual = manualBuilder.getResult()
print(manual)

builder = CarBuilder()
director.makeRandomCar(builder)
car2 = builder.getResult()
print(car2)
