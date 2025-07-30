## if we have __init__() in child class then the constructor of parent class will not called

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor !!!")
        self.__price=price
        self.brand=brand
        self.camera=camera

class SmartPhone(Phone):
    def __init__(self,os,ram):
        self.os=os
        self.ram=ram
        print("Inside SmartPhone Constructor !!")
    
s=SmartPhone('Android',12)
s.brand
