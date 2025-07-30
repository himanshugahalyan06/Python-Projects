def total_marks_percentage_grade():
    print("\n")
    roll_number = input("Enter roll number to calculate total marks , percentage and Grade: ")
    try:
        with open("Assessment_3\\Data_base\\student_record.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No records found!")
                return
            found = False
            for line in lines:
                name, roll, Physics, Maths, Chemistry = line.strip().split(",")  # Tuple Unpacking
                if roll_number == roll:
                    found = True
                    Physics = int(Physics)
                    Maths = int(Maths)
                    Chemistry = int(Chemistry)
                    Total_Marks = Physics + Maths + Chemistry
                    Percentage = (Total_Marks / 300) * 100

                # Grade Calculation
                    if Percentage >= 90:
                        Grade = 'A+'
                    elif Percentage >= 80:
                        Grade = 'A'
                    elif Percentage >= 70:
                        Grade = 'B'
                    elif Percentage >= 60:
                        Grade = 'C'
                    elif Percentage >= 50:
                        Grade = 'D'
                    else:
                        Grade = 'F'


                    print("\n---- Student Total Marks ----")
                    print(f"Student Name: {name}")
                    print(f"Roll Number: {roll}")
                    print(f"Total Marks: {Total_Marks}")
                    print(f"Percentage: {Percentage:.2f}%")
                    print(f"Grade: {Grade}")
                    break
            if not found:
                print("Roll number not found!")
    except FileNotFoundError:
        print("No records found!")


def menu():
    while True:
        print("\n")
        print("Student Data")
        print("1.Total Marks of Student")
        print("2.Exit")

        try:
            choice = int(input("Enter your Choice: (1-2): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 2.\n")
            continue

        if choice not in [1, 2]:
            print("❌ Invalid Choice! Please select from 1 to 2.\n")
            continue

        if choice == 1:
            total_marks_percentage_grade()
        elif choice==2:
            print("\n")
            print("---- Exit Section ----")
            exit_choice = input("Do you want to exit the program? (yes/no): ").strip().lower()
            if exit_choice == 'yes':
                print("Wishing you a wonderful day ahead! 😊")
                print("Goodbye! 👋")
                break
            else:
                print("\n🔁 Taking you back to the main menu... Let's continue! 🚀\n")



if __name__== "__main__":
    menu()



