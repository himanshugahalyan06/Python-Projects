## Polymorphism means same function name behaves differently in different classes

class Cat:
    def sound(self):
        print("meow")
class Dog:       
    def sound(self):
        print("bark")

def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Dog())
