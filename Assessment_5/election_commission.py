from voter import Voter
from candidate import Candidate

class ElectionCommission:
    def __init__(self):
        self.voters = {}
        self.candidates = {}

    def register_voter(self, name, age, voter_id):
        if voter_id in self.voters:
            print("Voter ID already registered!")
        elif age < 18:
            print("Voter must be 18 or older.")
        else:
            self.voters[voter_id] = Voter(name, age, voter_id)
            print("Voter registered successfully.")

    def register_candidate(self, name, age, party):
        if name in self.candidates:
            print("Candidate already registered!")
        else:
            self.candidates[name] = Candidate(name, age, party)
            print("Candidate registered successfully.")

    def vote(self, voter_id, candidate_name):
        if voter_id not in self.voters:
            print("Voter ID not found.")
            return
        if candidate_name not in self.candidates:
            print("Candidate not found.")
            return
        voter = self.voters[voter_id]
        if voter.voted:
            print("This voter has already voted.")
        else:
            self.candidates[candidate_name].votes += 1
            voter.voted = True
            print("Vote cast successfully!")

    def show_results(self):
        print("\n--- Election Results ---")
        winner = None
        max_votes = -1
        for candidate in self.candidates.values():
            candidate.display_info()
            if candidate.votes > max_votes:
                max_votes = candidate.votes
                winner = candidate
        print(f"\n🏆 Winner: {winner.name} from {winner.party} with {winner.votes} votes!")
