# def area_circle(r):
#     PI = 3.14
#     return PI * r ** 2

# def area_of_triangle(b, h):
#     return 0.5 * b * h

# def area_rectangle(l, b):
#     return l * b

# def main_menu():
#     while True:
#             print("\n")
#             print("---- Which Operation You Want to Perform ----")
#             print()
#             print("1.Area of circle ")
#             print("2.Area of Triangle ")
#             print("3.Area of Rectangle ")
#             print("4.exit")

#             choice=input("Enter your Choice between 1 to 4: ")

#             if choice=="1":
#                 r = float(input("Enter the radius: "))
#                 print("Area of Circle:", area_circle(r))
#             elif choice=="2":
#                 b = float(input("Enter the base: "))
#                 h = float(input("Enter the height: "))
#                 print("Area of Triangle:", area_of_triangle(b, h))
#             elif choice=="3":
#                 l = float(input("Enter the length: "))
#                 b = float(input("Enter the width: "))
#                 print("Area of Rectangle:", area_rectangle(l, b))
#             elif choice=="4":
#                 print("\n")
#                 print("---- Exit Section ----")
#                 exit_choice = input("Do you want to exit the program? (yes/no): ").strip().lower()
#                 if exit_choice == 'yes':
#                     print("Wishing you a wonderful day ahead! 😊")
#                     print("Goodbye! 👋")
#                     break
#                 else:
#                     print("\n🔁 Taking you back to the main menu... Let's continue! 🚀\n")

# if __name__=="__main__":
#     main_menu()


def area_circle(r):
    PI = 3.14
    return PI * r ** 2

def area_of_triangle(b, h):
    return 0.5 * b * h

def area_rectangle(l, b):
    return l * b

def is_perfect_number(n):
    if n < 1:
        return False
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def main_menu():
    while True:
        print("\n")
        print("---- Which Operation You Want to Perform ----")
        print()
        print("1. Area of Circle ")
        print("2. Area of Triangle ")
        print("3. Area of Rectangle ")
        print("4. Check Perfect Number ")
        print("5. Check Prime Number ")
        print("6. Check Palindrome Number ")
        print("7. Exit")

        choice = input("Enter your Choice between 1 to 7: ")

        if choice == "1":
            r = float(input("Enter the radius: "))
            print("Area of Circle:", area_circle(r))
        elif choice == "2":
            b = float(input("Enter the base: "))
            h = float(input("Enter the height: "))
            print("Area of Triangle:", area_of_triangle(b, h))
        elif choice == "3":
            l = float(input("Enter the length: "))
            b = float(input("Enter the width: "))
            print("Area of Rectangle:", area_rectangle(l, b))
        elif choice == "4":
            num = int(input("Enter a number to check if it's a Perfect Number: "))
            if is_perfect_number(num):
                print(f"{num} is a Perfect Number.")
            else:
                print(f"{num} is NOT a Perfect Number.")
        elif choice == "5":
            num = int(input("Enter a number to check if it's a Prime Number: "))
            if is_prime(num):
                print(f"{num} is a Prime Number.")
            else:
                print(f"{num} is NOT a Prime Number.")
        elif choice == "6":
            num = int(input("Enter a number to check if it's a Palindrome Number: "))
            if is_palindrome(num):
                print(f"{num} is a Palindrome Number.")
            else:
                print(f"{num} is NOT a Palindrome Number.")
        elif choice == "7":
            print("\n")
            print("---- Exit Section ----")
            exit_choice = input("Do you want to exit the program? (yes/no): ").strip().lower()
            if exit_choice == 'yes':
                print("Wishing you a wonderful day ahead! 😊")
                print("Goodbye! 👋")
                break
            else:
                print("\n🔁 Taking you back to the main menu... Let's continue! 🚀\n")
        else:
            print("\n⚠️ Invalid choice! Please enter a number between 1 and 7.\n")

if __name__ == "__main__":
    main_menu()
