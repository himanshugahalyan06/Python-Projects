class Person:
    def __init__(self,Name,Country):
        self.Name=Name
        self.Country=Country
        print("Address of Self: ",(id(self)))


    def greet(self):
        if self.Country=='India':
            print("Namaste",self.Name)
        else:
            print("Hello",self.Name)

x=input("Enter your Name: ")
y=input("Enter you Country: ")

P=Person(x,y)
print("Address of Object: ",(id(P)))
P.greet()  

P.Name   # Access the Attrinutes outside the class using object 
P.Country  

## Create a attribute outside the 
P.Gender='Male'
P.Name='Raj' 

print(P.Name)
print(P.Country)

# we use encapsulation to handle the issue of creating the attributes outside the class 
# because if we make a attribute of same (name) outside the class this will affect the value of attribute inside the class 
# we cannot access the value of attribute inside the class because the value is changed by new one 
# to slove this issue we have to make attrinute/variable private inside the class 

# when we make a member private then python automattically change the name of that variable in member location 
# # python change name like syntax: (oject name._class name__variable name) 

# make private (__variable name)





