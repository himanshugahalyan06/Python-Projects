from person import *

class Voter(Person):
    def __init__(self,name,age,voter_id):
        super().__init__(name,age)
        self.voter_id=voter_id
        self.voted=False  

    def display_info(self):
        print(f"Voter ID: {self.voter_id}, Name: {self.name}, Age: {self.age}, Voted: {self.voted}")