## If the parent class and child class each have a method with the same name and definition(must not be same but paramters must be same ) ,
## the method inside the child class called first when you 
## create the object of child class 
# if make a object od child then it just display child attributes not parent and vice versa
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
    
s=SmartPhone(20000,'Samsung',3)
s.buy()
# p=Phone(20000,'Vivo',5)
# p.buy()