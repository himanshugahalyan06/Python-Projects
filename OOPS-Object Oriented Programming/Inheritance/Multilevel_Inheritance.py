#Grandfather class (Base class)
class Grandfather:
    def house(self):
        print("Grandfather has a big houde ")

# Father class (inherits from Grandfather)
class Father(Grandfather):
    def car(self):
        print("Father has a car")

# Child class (inherits from Father)
class Child(Father):
    def bike(self):
        print("Child has a bike")

# Create object of Child
c = Child()

# Call methods from all classes
c.house()  # From Grandfather
c.car()       # From Father
c.bike()    # From Child