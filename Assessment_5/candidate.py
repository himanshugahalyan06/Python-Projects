from person import *

class Candidate(Person):
    def __init__(self, name, age, party):
        super().__init__(name, age)
        self.party = party
        self.votes = 0

    def display_info(self):
        print(f"Candidate: {self.name}, Age: {self.age}, Party: {self.party}, Votes: {self.votes}")
