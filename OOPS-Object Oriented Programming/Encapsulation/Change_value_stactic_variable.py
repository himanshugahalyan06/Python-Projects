#changing the value of static variable
class Employee:
    company = "TechCorp" # Static variable
    def __init__(self, name, salary):
        self.name = name
    # Instance variable
        self.salary = salary
    # Instance variable
    # Create employee objects
e1 = Employee ("John", 50000)
e2 = Employee("Jane", 60000)
    # Accessing static and instance variables
print(e1.name, e1. salary, e1. company) #John 50000 TechCorp 
print(e2. name, e2. salary, e2. company) # Jane 60000 TechCorp
    # Changing static variable
Employee.company = "Google"

print(e1.company)
print(e2.company)
# changing instance variable
e1.salary=55000
print(e1.salary)  # 55000
print(e2.salary)   # 60000

