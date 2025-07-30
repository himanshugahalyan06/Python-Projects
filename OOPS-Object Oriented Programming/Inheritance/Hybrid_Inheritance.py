#Hybrid Inheritance
#THis is a mix of More than One type
class A:
    def feature1 (self):
        print("Feature 1 from class A")

class B(A):
    def feature2 (self):
        print("Featutre 2 from class B")

class C(A):
    def feature3 (self):
        print("Feature 3 from class C")

class D(B,C):
    def feature4 (self):
        print("Feature 4 from class D")

obj = D()
obj.feature1()
obj.feature2()
obj.feature3()
obj.feature4()