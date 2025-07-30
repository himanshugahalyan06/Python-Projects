## if we don't have __init__() in child then the __init__() of parent will called first 
class Parent:
    def __init__(self,num):
        self.__num=num
        
        ## getter method
    def get_num(self):
        print(self.__num)

class Child(Parent):
    def show(self):
        print("This is in Child Class !! ")
    
    
son=Child(100)
son.get_num()
son.show()