## child can't access the private member of the class 
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor !!!")
        self.__price=price
        self.brand=brand
        self.camera=camera

        ## getter method
    def show(self):
        print(self.__price)

class SmartPhone(Phone):
    def check(self):
        print(self.__price)
    
s=SmartPhone(20000,'Android',12)
s.show()
