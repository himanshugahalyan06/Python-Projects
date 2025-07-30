# Module these are the function that are wrtting by and user and anyone can imoort that module in there code 
# Module is a python file whcih contain some definitions 
# It's advantages are 

def surface_area_cube(a):
    return 6*a**2

def volume_cube(a):
    return a**3

def surface_area_cuboid(l,b,h):
    return 2*(l*b + b*h + h*l)

def volume_cuboid(l,b,h):
    return (l*b*h)

def surface_area_cylinder(PI,r,h):
    PI=3.14
    return 2*PI*r*(h+r)

def volume_cylinder(PI,r,h):
    PI=3.14
    return PI*r**2*h

def surface_cone(PI,r,l):
    PI=3.14
    return PI*r*(l+r)

def volume_cone(PI,r,h):
    PI=3.14
    return 1/3*PI*r**2*h

def surface_area_sphere(PI,r):
    PI=3.14
    return 4*PI*r**2

def volume_sphere(PI,r):
    PI=3.14
    return 4/3*PI*r**3

def surface_area_hemisphere(PI,r):
    PI=3.14
    return 3*PI*r**2

def volume_hemisphere(PI,r):
    PI=3.14
    return 2/3*PI*r**3

def main_menu():
    while True:
        print("\n")
        print("---- Which Operation Ypu Want to Perform ----")
        print()
        print("1. Surface area of Cube ")
        print("2. Volume of Cube ")
        print("3. Surface area of Cuboid ")
        print("4. Volume of Cuboid ")
        print("5. Surface area of Cylinder ")
        print("6. Volume of Cylinder ")
        print("7. Surface area of Cone ")
        print("8. Volume of Cone")
        print("9. Surface area of Sphere ")
        print("10. Volume  of Shphere ")
        print("11. Surface area of Hemisphere ")
        print("12. Volume of Hemisphere ")
        print("13. Exit")

        try:
            choice = int(input("Enter your Choice: (1-13): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 13.\n")
            continue

        if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
            print("❌ Invalid Choice! Please select from 1 to 13.\n")
            continue

        if choice == 1:
            a = int(input("Enter the side: "))      # Take input here
            result = surface_area_cube(a)           # Pass 'a' as argument correctly
            print("Surface area of Cube is: ", result)  # Display the result here
        elif choice == 2:
            a = int(input("Enter the side: "))     
            result = volume_cube(a)           
            print("Volume of Cube is: ", result)  
        elif choice == 3:
            l=int(input("Enter Length: "))
            b=int(input("Enter Width: "))
            h=int(input("Enter Height: "))     
            result = surface_area_cuboid(l,b,h)           
            print("Surface area of Cuboid is: ", result)  
        elif choice == 4:
            l=int(input("Enter Length: "))
            b=int(input("Enter Width: "))
            h=int(input("Enter Height: "))     
            result = volume_cuboid(l,b,h)           
            print("Volume of Cuboid is: ", result)  
        elif choice == 5:
            PI=3.14
            r=float(input("Enter Radius: "))
            h=float(input("Enter Height: "))
            result=surface_area_cylinder(PI,r,h)
            print("Surface area of Cylinder: ",result)
        elif choice==6:
            PI=3.14
            r=float(input("Enter Radius: "))
            h=float(input("Enter Height: "))
            result=surface_area_cylinder(PI,r,h)
            print("Volume of Cylinder: ",result)
        elif choice==7:
            PI=3.14
            r=float(input("Enter Radius: "))
            l=float(input("Enter Length: "))
            result=surface_cone(PI,r,l)
            print("Surface area of Cone: ",result)
        elif choice==8:
            PI=3.14
            r=float(input("Enter Radius: "))
            l=float(input("Enter Length: "))
            result=volume_cone(PI,r,l)
            print("Surface area of Cone: ",result)
        elif choice==9:
            result=surface_area_sphere(PI,r)
            PI=3.14
            r=float(input("Enter Radius: "))
            print("Surface area of Sphere: ",result)
        elif choice==10:
            result=volume_sphere(PI,r)
            PI=3.14
            r=float(input("Enter Radius: "))
            print("Volume of Sphere: ",result)
        elif choice==11:
            PI=3.14
            r=float(input("Enter Radius: "))
            result=surface_area_hemisphere(PI,r)
            print("Surface area of Hemisphere: ",result)
        elif choice==12:
            PI=3.14
            r=float(input("Enter Radius: "))
            result=volume_hemisphere(PI,r)
            print("Volume of Hemisphere: ",result)
        elif choice==13:
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



