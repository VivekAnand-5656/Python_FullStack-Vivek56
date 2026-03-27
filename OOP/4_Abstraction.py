# ============== Abstraction =================

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self): 
        print("Car Start with key")

class Bike(Vehicle):
    def start(self): 
        print("Bike Start wth Kick")
c = Car()
c.start()
b = Bike()
b.start()