# this is known as class variable it is declared inside the class but outside all metods 
# accessing using class name.variable name or self.variable name

class Student:
    college='Geeta University'   # static variable
    def __init__(self,name):
        self.name=name  # instance variable


s1=Student("Alice")
s2=Student("Bob")

print(s1.name,s1.college)
print(s2.name,s2.college)

