class Parent:
    def show(self):
        print("this is a parent class")

class Son(Parent):
    def son_info(self):
        print("this is the son class")

class Daughter(Parent):
    def daughter_info(self):
        print("This is the Daughter Class !!")

s=Son()
d=Daughter()

s.son_info()
d.daughter_info()