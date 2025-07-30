# When We Read a file line by line then all tha values are by default string 

# Dictionary for student data 
student_data = {
    1003: {'name': 'Aarav', 'Physics': 85, 'Maths': 92, 'Chemistry': 88},
    1004: {'name': 'Isha', 'Physics': 78, 'Maths': 81, 'Chemistry': 85},
    1005: {'name': 'Vivaan', 'Physics': 90, 'Maths': 87, 'Chemistry': 91},
    1006: {'name': 'Diya', 'Physics': 72, 'Maths': 75, 'Chemistry': 70},
    1007: {'name': 'Arjun', 'Physics': 88, 'Maths': 85, 'Chemistry': 84},
    1008: {'name': 'Meera', 'Physics': 76, 'Maths': 79, 'Chemistry': 80},
    1009: {'name': 'Kabir', 'Physics': 95, 'Maths': 89, 'Chemistry': 94},
    1010: {'name': 'Anaya', 'Physics': 83, 'Maths': 86, 'Chemistry': 80},
    1011: {'name': 'Rohan', 'Physics': 65, 'Maths': 70, 'Chemistry': 68},
    1012: {'name': 'Priya', 'Physics': 91, 'Maths': 88, 'Chemistry': 90}
}


# Function to add data direct from Dictionary without user input 
def add_data_from_dict(student_data):
    with open("Assessment_3\\Data_base\\student_record.txt", "a") as file:  # "a" to append
        for roll, student in student_data.items():  # Correct loop for nested dictionary
            file.write(f"{student['name']},{roll},{student['Physics']},{student['Maths']},{student['Chemistry']}\n")
print("\n")
print("All student records written successfully!")



# Function to add students
def add_students():
    student_data['name'] = input("Enter your name: ").strip().title()
    student_data['roll']=int(input("Enter your roll_number: "))
    student_data['Physics']=int(input("Enter Your Marks in Physics : "))
    student_data['Maths']=int(input("Enter Your Marks in Maths: "))
    student_data['Chemistry']=int(input("Enter Your Marks in Chemistry: "))
    print("Student Data Added Successfully !!")

    with open("Assessment_3\\Data_base\\student_record.txt", "a") as file:
        # Write in comma-separated format
        file.write(f"{student_data['name']},{student_data['roll']},{student_data['Physics']},{student_data['Maths']},{student_data['Chemistry']}\n")


# Function to display students according to roll_number 
def display_all():
    print("\n")
    print("---- All student record ----")
    print()
    try:
        with open("Assessment_3\\Data_base\\student_record.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No records found !!.")
                return
            for line in lines:
                name, roll, Physics, Maths, Chemistry = line.strip().split(",")
                print(f"Name: {name}, Roll No: {roll}, Physics: {Physics}, Maths:{Maths}, Chemistry: {Chemistry}")
    except FileNotFoundError:
        print("No records found.\n")


# Function to search students with there roll number 

def search_student():
    roll_number=int(input("Enter Roll_Number you want to search: "))
    try:
        with open("Assessment_3\\Data_base\\student_record.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No roll_number found !!.")
                return
            for line in lines:
                name, roll, Physics, Maths, Chemistry = line.strip().split(",")
                if roll_number==roll:
                    print(f"Name: {name}, Roll No: {roll}, Physics: {Physics}, Maths:{Maths}, Chemistry: {Chemistry}")
    except FileNotFoundError:
        print("Record Not Found !!")
    

# Function to Update the Information 
def update_student():
    roll_number = int(input("Enter roll number to update: "))
    updated = False
    try:
        with open("Assessment_3\\Data_base\\student_record.txt", "r") as file:
            lines = file.readlines()

        with open("Assessment_3\\Data_base\\student_record.txt", "w") as file:
            for line in lines:
                name, roll, Physics, Maths, Chemistry = line.strip().split(",")
                if roll_number == roll:
                    print(f"Current Marks -> Physics: {Physics}, Maths-> {Maths}, Chemistry-> {Chemistry}")
                    Physics = int(input("Enter new Physics marks: "))
                    Maths = int(input("Enter new Maths marks:"))
                    Chemistry =int(input("Enter new Chemistry marks:"))
                    file.write(f"{name},{roll},{Physics},{Maths},{Chemistry}\n")
                    updated = True
                else:
                    file.write(line)
        
        if updated:
            print(" Student marks updated successfully !!!! ")
        else:
            print(" Roll number not found !!!! ")
    except FileNotFoundError:
        print("No records found !!!! ")
                    


# Function to delete the entry               
def delete_student():
    roll_number = input("Enter roll number to deleted:")
    deleted = False
    try:
        with open("Assessment_3\\Data_base\\student_record.txt","r") as file:
            lines = file.readlines()
        with open("Assessment_3\\Data_base\\student_record.txt","w") as file:
            for line in lines:
                name , roll, *_=line.strip().split(",")
                if roll_number != roll:
                    file.write(line)
                else:
                    deleted = True
        if deleted:
            print(" Student record deleted successfully !!!! ")
        else:
            ("Roll number not found !!!! ")
    except FileNotFoundError:
        print(" No records to delete !!!! ")  



# Menu system
def main_menu():
    while True:
        print("\n")
        print("---- Student Report Card System ----")
        print()
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student by Roll No")
        print("4. Update Student Marks")
        print("5. Delete Student Record")
        print("6. Add Data Direct From Dictionary Without User Input")
        print("7. Exit")

        try:
            choice = int(input("Enter your Choice: (1-7): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 7.\n")
            continue

        if choice not in [1, 2, 3, 4, 5, 6,7]:
            print("❌ Invalid Choice! Please select from 1 to 7.\n")
            continue

        if choice == 1:
            add_students()
        elif choice == 2:
            display_all()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice==6:
            add_data_from_dict(student_data)
        elif choice==7:
            print("\n")
            print("---- Exit Section ----")
            exit_choice = input("Do you want to exit the program? (yes/no): ").strip().lower()
            if exit_choice == 'yes':
                print("Wishing you a wonderful day ahead! 😊")
                print("Goodbye! 👋")
                break
            else:
                print("\n🔁 Taking you back to the main menu... Let's continue! 🚀\n")

# This condition ensures the main_menu() function runs only if this script is the main program being executed.

if __name__ == "__main__":
    main_menu()
