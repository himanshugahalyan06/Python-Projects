# Aggregation 
class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
        
    def print_address(self):
        print(self.address.city, self.address.state, self.address.pin)

class Address:
    def __init__(self,city,state,pin):
        self.city = city
        self.state = state
        self.pin = pin

add  = Address("Sonipat","Harayana",131001)
cust = Customer("Gopal","male",add)
cust.print_address()