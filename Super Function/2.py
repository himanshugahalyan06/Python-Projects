class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor !!!")
        self.__price=price
        self.brand=brand
        self.camera=camera
        print("Brand: ",brand)

    def buy(self):
        print("Buying a Phone !!")
    
class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smart Phone !!")
    
s=SmartPhone(20000,'Samsung',3)
s.buy()