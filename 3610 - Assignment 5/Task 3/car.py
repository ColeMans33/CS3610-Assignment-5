from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self.seats = 0
        self.engine = ""
        self.tripComputer = False
        self.gps = False

    def __str__(self):
        return f"Seats: {self.seats}\nEngine: {self.engine}\nTrip Computer: {self.tripComputer}\nGPS: {self.gps}"
