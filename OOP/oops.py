# Object Oriented Programming

# Inheritance
    # Leverage

# Polymorphism
    # Behavior
    # override
    # overload - functions  variable length parameter

# Abstraction
    # enforce restriction

# Encapsulation
    # hiding inner details

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def drive(self):
        print("Drive")

class Car(Vehicle):
    
    def start(self):
        print("Car Running")
        # super().start()

    def stop():
        print("Car Stopped")

class Truck(Vehicle):
    def start(self):
        print("Truck Started")

    def stop(self):
        print("Truck Stopped")

truck = Truck()
truck.start()

car_one = Car()
car_one.start()
car_one.stop()
