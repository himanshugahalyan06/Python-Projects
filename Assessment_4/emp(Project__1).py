import datetime

# Base employee with punch-in and punch-out tracking
class Employee:
    def __init__(self, empid, name, department):
        self.empid = empid
        self.name = name
        self.department = department
        self.punch_time = datetime.datetime.now()  # punch-in
        self.punch_out = self.punch_time + datetime.timedelta(hours=8)  # Fixed punch-out after 8 hours

    def work_duration(self):
        return self.punch_out - self.punch_time

    def display(self):
        entry = self.punch_time.strftime("%Y-%m-%d %H:%M:%S")
        exit_time = self.punch_out.strftime("%Y-%m-%d %H:%M:%S")
        duration = str(self.work_duration())
        print(f"{self.empid} --> {self.name}\n[{self.department}]\nIn: {entry}\nOut: {exit_time}\nWorked: {duration}", end="")

# Full-time employee — fixed salary
class FullTime(Employee):
    def __init__(self, empid, name, dept, salary):
        super().__init__(empid, name, dept)
        self.salary = salary

    def display(self):
        super().display()
        print(f"\nSalary: ₹{self.salary}")

# Part-time with overtime beyond 8 hours/day
class PartTime(Employee):
    def __init__(self, empid, name, dept, hours_worked):
        super().__init__(empid, name, dept)
        self.RATE = 200
        self.hours = hours_worked
        self.punch_out = self.punch_time + datetime.timedelta(hours=hours_worked)  

    def calculate_pay(self):
        reg_hours = min(self.hours, 8)
        ot_hours = max(0, self.hours - 8)
        regular = reg_hours * self.RATE
        overtime = ot_hours * self.RATE * 1.5
        return regular + overtime

    def display(self):
        pay = self.calculate_pay()
        super().display()
        print(f"\nRate: ₹{self.RATE}, Hours: {self.hours} → Pay: ₹{pay:.2f}")

# Intern with stipend
class Intern(Employee):
    def __init__(self, empid, name, dept, college, stipend):
        super().__init__(empid, name, dept)
        self.college = college
        self.stipend = stipend

    def display(self):
        super().display()
        print(f"\nCollege: {self.college}, Stipend: ₹{self.stipend}")


full=FullTime(1001, "ABC", "Engineering", 60000)
part=PartTime(1002, "XYZ", "Support", 10)
intern=Intern(1003, "JLK", "Marketing", "State Univ", 1000)

# Main function
def main():
    while True:
        print("---- Employee Management System ----")
        print()
        print("1. Full Time !!")
        print("2. Part Time !!")
        print("3. Intern !!")
        print("4. Exit")

        try:
            choice = int(input("Enter your Choice: (1-4): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 4.\n")
            continue

        if choice not in [1, 2, 3, 4]:
            print("❌ Invalid Choice! Please select from 1 to 4.\n")
            continue

        if choice == 1:
            full.display()
        elif choice == 2:
            part.display()
        elif choice == 3:
            intern.display()
        elif choice == 4:
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
