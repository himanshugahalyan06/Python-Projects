## method wuth same name but different parameters list 

class Shape:
    def area(self,a,b=0):
        if b==0:
            return 3.14*a*2
        else:
            return a*b
s=Shape()
print(s.area(2))
print(s.area(3,4))