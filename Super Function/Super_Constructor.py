class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor !!!")
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a Phone !!")
    
class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("Inside Smartphone Constructor")

s=SmartPhone(20000,'Samsung',3,'Android',12)
print(f"Operating System is: {s.os}\nBrand is: {s.brand}")