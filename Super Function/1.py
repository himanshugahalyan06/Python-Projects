class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor !!!")
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a Phone !!")
    
class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smart Phone !!")
        # syntax to call parent ka buy method inside the class
        super().buy()
    
s=SmartPhone(20000,'Samsung',3)
s.buy()