# Dictionary for employee data 
employee_data = {
    1001: {'name': 'Himanshu', 'department': 'IT', 'salary': 500000},
    1002: {'name': 'Alisha', 'department': 'HR', 'salary': 600000},
    1003: {'name': 'Muskan', 'department': 'HR', 'salary': 500000},
    1004: {'name': 'Sahil', 'department': 'Finance', 'salary': 600000},
    1005: {'name': 'Gopal', 'department': 'IT', 'salary': 75000},
    1006: {'name': 'Diya', 'department': 'Marketing', 'salary': 52000},
    1007: {'name': 'Arjun', 'department': 'Operations', 'salary': 58000},
    1008: {'name': 'Meera', 'department': 'Sales', 'salary': 61000},
    1009: {'name': 'Kabir', 'department': 'IT', 'salary': 80000},
    1010: {'name': 'Anaya', 'department': 'Finance', 'salary': 63000},
    1011: {'name': 'Rohan', 'department': 'HR', 'salary': 48000},
    1012: {'name': 'Priya', 'department': 'Marketing', 'salary': 70000}
}

# Function to add data direct from Dictionary without user input 
def add_employee_data_from_dict(employee_data):
    with open("Assessment_3_project_2\\Data_base\\employee_record.txt", "a") as file:  # "a" to append
        for employee_id, employee in employee_data.items():  # Correct loop for nested dictionary
            file.write(f"{employee['name']},{employee_id},{employee['department']},{employee['salary']}\n")
    print("\nAll Employee records written successfully!")


# Function to add students
def add_employee():
    employee_data['name'] = input("Enter your name: ").strip().title()
    employee_data['employee_id']=int(input("Enter your employee_id: "))
    employee_data['department']=int(input("Enter Your Department : "))
    employee_data['salary']=float(input("Enter Your Salary: "))
    print("Employee Data Added Successfully !!")

    with open("Assessment_3_project_2\\Data_Base\\employee_record.txt", "a") as file:
        # Write in comma-separated format
        file.write(f"{employee_data['name']},{employee_data['employee_id']},{employee_data['department']},{employee_data['salary']}\n")


