class Animal:   # Parent class
    def speak (self):
        print("Animal Make Sound !!")


class Dog(Animal):
    def sound(self):
        print("Dog Bark !!")

## Onject
d=Dog()
d.speak()
d.sound()


## code 2 

class Rectangle:
    def __init__(self):
        self.l=2
        self.b=4

    def area(self):
        print("Area of Rectangle: ",self.l*self.b)

class Cuboid(Rectangle):
    def volume(self):
        self.h=6
        print("The Volume is: ",self.l*self.h*self.b)

c=Cuboid()
c.volume()
c.area()


## Code 3

class Rectangle:
    def area(self,l,b):
        self.l=l
        self.b=b
        print("Area of Rectangle: ",self.l*self.b)

class Cuboid(Rectangle):
    def volume(self,h):
        Rectangle.__init__(self)
        self.h=h
        print("The Volume is: ",self.l*self.h*self.b)

l=int(input("Enter Length: "))
b=int(input("Enter Width: "))
h=int(input("Enter Height: "))


c=Cuboid()
c.area(l,b)
c.volume(h)


## code 4 

class Rectangle:
    def __init__(self):
        self.l=l
        self.b=b
        print("Area of Rectangle: ",self.l*self.b)

class Cuboid(Rectangle):
    def __init__(self):
        Rectangle.__init__(self)
        self.h=h
        print("The Volume is: ",self.l*self.h*self.b)

l=int(input("Enter Length: "))
b=int(input("Enter Width: "))
h=int(input("Enter Height: "))

c=Cuboid(l,b,h)