from abc import ABC, abstractmethod

#may need to a list type for the manual instead so the client can create more details like type of seats, how to maintian engine, tuples?
#currently not implemented because the diagram shows nothing extra being passed in the manual builder
class Manual:
  def __init__(self):
    self.seats = 0
    self.engine = ""
    self.tripComputer = False
    self.gps = False

  def __str__(self):
    return f"Your brand new car contains: \n Seats: {self.seats} \n Engine: {self.engine}\n Trip Computer: {self.tripComputer}\n GPS: {self.gps}\n \n Table of contents......"
