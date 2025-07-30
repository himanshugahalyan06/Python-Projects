## What gets inherited 
## constructor , non private attributes , non private methods 

## code 
class Phone:
    def __init__(self,price,brand,camera):
        print("Indide phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy (self):
        print("Buying a phone")

class SmartPhone(Phone):
    print("Inside smartphone !!")
s=SmartPhone(20000,'Apple',13)
s.buy()
