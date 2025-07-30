# Reference variable hold objects
# we can create object without reference variable as well 
# an onject can have mutliple refernce variable 
# assinging a new refernce variable to an existing object does not create a new object 


### Object without a reference 
class Person:
    def __init__(self):
        self.name='XYZ'
        self.gender='Male'

p=Person()
print(p.name)
q=Person() ## q is reference variable for p
print(q.gender)

q.name="Himanshu"

print(q.name)
print("Address of P: ",(id(p)))
print("Address of Q: ",(id(q)))