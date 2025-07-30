from abc import ABC,abstractmethod
class Shape(ABC):
    @ abstractmethod
    def area(self):
        pass
    def info(self):
        print("This is a Shape !!")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self): ## overriding of abstract method 
        return 3.14*self.radius*self.radius 
    
c=Circle(5)
c.info()
print("Area of the Circle: ",c.area())