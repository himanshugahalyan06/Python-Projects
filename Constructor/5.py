class Parent:
    def __init__(self,num):
        self.__num=num
        
        ## getter method
    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self,val,num):
        self.__val=val

    def get_val(self):
        return self.__val
    
    
son=Child(100,10)
print("Child Val",son.get_val())
print("Parent Num",son.get_num())