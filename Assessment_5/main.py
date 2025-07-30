from election_commission import ElectionCommission

def main():
    ec = ElectionCommission()

    while True:
        print("\n--- Parliamentary Election 2024 ---")
        print("1. Register Voter")
        print("2. Register Candidate")
        print("3. Cast Vote")
        print("4. Show Results")
        print("5. Exit")

        try:
            choice = int(input("Enter your Choice: (1-5): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 5.\n")
            continue

        if choice not in [1, 2, 3, 4,5]:
            print("❌ Invalid Choice! Please select from 1 to 5.\n")
            continue

        if choice == 1:
            Total_Voter=int(input("Enter the Number: "))
            print(f"Total Number of Voter to be Registered are: {Total_Voter} ")
            for i in range(Total_Voter):
                name = input("Enter Voter Name: ")
                age = int(input("Enter Age: "))
                voter_id = input("Enter Voter ID: ")
                ec.register_voter(name, age, voter_id)

        elif choice == 2:
            Total_Candidate=int(input("Enter the Number: "))
            print(f"Total Number of Candidate to be Registered are: {Total_Candidate} ")
            for i in range(Total_Candidate):
                name = input("Enter Candidate Name: ")
                age = int(input("Enter Age: "))
                party = input("Enter Party: ")
                ec.register_candidate(name, age, party)

        elif choice == 3:
            for i in range(Total_Voter):
                voter_id = input("Enter Voter ID: ")
                candidate_name = input("Enter Candidate Name to Vote For: ")
                ec.vote(voter_id, candidate_name)

        elif choice == 4:
            ec.show_results()

        elif choice == 5:
            print("\n")
            print("---- Exit Section ----")
            exit_choice = input("Do you want to exit the program? (yes/no): ").strip().lower()
            if exit_choice == 'yes':
                print("Wishing you a wonderful day ahead! 😊")
                print("Goodbye! 👋")
                break
            else:
                print("\n🔁 Taking you back to the main menu... Let's continue! 🚀\n")

if __name__ == "__main__":
    main()
