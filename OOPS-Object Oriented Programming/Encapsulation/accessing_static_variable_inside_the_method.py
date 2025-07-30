class Counter:
    count=0   # stactic variable

    def __init__(self):
        Counter.count+=1
    @classmethod
    def get_count(cls):
        return cls.count
        
# in this king of call we call methods by class name not by object name

# create objects
c1=Counter()
c2=Counter()
c3=Counter()
c4=Counter()
print("The Count is: ",Counter.get_count())  # output: 4 it is always equal to number of object we made 


# uderstand using Python Tutior 