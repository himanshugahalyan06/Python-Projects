from abc import ABC ,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def move(slef):
        pass 

class Dog(Animal):
    def sound(self):
        print("Bark !!")
    def move (self):
        print("Run !!")

d=Dog()
d.sound()
d.move()