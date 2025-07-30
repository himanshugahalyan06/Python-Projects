# Function to display students according to roll_number 
from employee import *

def display_all():
    print("\n")
    print("---- All student record ----")
    print()
    try:
        with open("Assessment_3_project_2\\Data_Base\\employee_record.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No records found !!.")
                return
            for line in lines:
                name, employee_id, department, salary = line.strip().split(",")
                print(f"{name},{employee_id},{department},{salary}")

    except FileNotFoundError:
        print("No records found.\n")


# Function to search students with there roll number 

def search_employee():
    emp_id=int(input("Enter Employee_id you want to search: "))
    try:
        with open("Assessment_3_project_2\\Data_Base\\employee_record.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No Record found !!.")
                return
            for line in lines:
                name, employee_id, department, salary = line.strip().split(",")
                if emp_id==employee_id:
                    print(f"{name},{employee_id},{department},{salary}")

    except FileNotFoundError:
        print("Record Not Found !!")
    

# Function to Update the Information 
def update_employee():
    emp_id = int(input("Enter Employee_Id to update: "))
    updated = False
    try:
        with open("Assessment_3_project_2\\Data_Base\\employee_record.txt", "r") as file:
            lines = file.readlines()

        with open("Assessment_3_project_2\\Data_Base\\employee_record.txt", "w") as file:
            for line in lines:
                name, employee_id, department, salary = line.strip().split(",")
                if emp_id == employee_id:
                    print(f"Current Satus -> Employee_Id: {employee_id}, Department-> {department}, Salary-> {salary}")
                    employee_id=int(input("Enter your employee_id: "))
                    department=int(input("Enter Your Department : "))
                    salary=float(input("Enter Your Salary: "))
                    file.write(f"{name},{employee_id},{department},{salary}\n")
                    updated = True
                else:
                    file.write(line)
        
        if updated:
            print(" Employee Data updated successfully !!!! ")
        else:
            print(" Employee_id not found !!!! ")
    except FileNotFoundError:
        print("No records found !!!! ")
                    


# Function to delete the entry               
def delete_employee():
    emp_id = input("Enter Employee_Id to deleted:")
    deleted = False
    try:
        with open("Assessment_3_project_2\\Data_Base\\employee_record.txt","r") as file:
            lines = file.readlines()
        with open("Assessment_3_project_2\\Data_Base\\employee_record.txt","w") as file:
            for line in lines:
                name , employee_id, *_=line.strip().split(",")
                if emp_id != employee_id:
                    file.write(line)
                else:
                    deleted = True
        if deleted:
            print(" Employee record deleted successfully !!!! ")
        else:
            (" Employee Id not found !!!! ")
    except FileNotFoundError:
        print(" No records to delete !!!! ")  



# Menu system
def main_menu():
    while True:
        print("\n")
        print("---- Employee Management System ----")
        print()
        print("1. Add Employee")
        print("2. Display All Records")
        print("3. Search Student by Employee_Id")
        print("4. Update Employee Record")
        print("5. Delete Employee Record ")
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
            add_employee()
        elif choice == 2:
            display_all()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            update_employee()
        elif choice == 5:
            delete_employee()
        elif choice==6:
            add_employee_data_from_dict(employee_data)
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
    
