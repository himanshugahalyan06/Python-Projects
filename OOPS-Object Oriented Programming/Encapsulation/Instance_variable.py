class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll


# create objects     ## it is known as object variable 
s1=Student("ABC",101)
s2=Student("XYZ",102)


print(s1.name,s1.roll)
print(s2.name,s2.roll)
