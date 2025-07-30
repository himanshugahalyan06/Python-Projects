class Person:
    def __init__(self,name):
        self.name=name
        print("Person class constructor !!")

class Student(Person):
    def __init__(self,name,roll):
        super.__init__(name)
        self.roll=roll
        print("Students class constructor !!")

s=Student("Rahul",101)