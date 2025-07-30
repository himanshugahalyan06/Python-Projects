from abc import ABC,abstractmethod

## Abstract class with one Abstract Method 

class Vehicle(ABC):
    @ abstractmethod
    def start_engine(self):
        pass 
class Car(Vehicle):
    def start_engine(self):
        print("Car Engine Started !!")

# obj=Vehicle()  --> show error 

my_car=Car()
my_car.start_engine()