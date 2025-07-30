from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_info(self):
        pass

