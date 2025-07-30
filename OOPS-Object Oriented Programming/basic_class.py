## Class name is always in Pascal case it means initial letter is capital like MyClass
## write (__/Double underscore) to make member private
# BY default all members are Public
# write (_/single underscore) to make member protected 

import time as t
class Atm:
    def __init__(self): # constructor complusory for every class and pass self as argument 
        # write self in front of attributes which we make in constructor only 
        self.pin=''
        self.balance=10000000
        self.account_num='0000'
        self.menu()

    def create_pin(self):
        ac_input=input("Enter your account no: ")
        if self.account_num==ac_input:
            input_pin=input("Enter four digit Pin: ")
            self.pin=input_pin
            print("Your Pin created successfully !!")
        else:
            print("Wrong Account Number !!")
    
    def change_pin(self):
        old_pin=input("Enter your old pin: ")
        if old_pin == self.pin:
            new_pin=input("Enter Your New Pin: ")
            self.pin = new_pin
            print("Your Pin Changed Successfully !!")
        else:
            print("Wrong Pin !! Enter Correct Pin !!")

    def check_balance(self):
        attempts=0
        while attempts < 3:
            enter_pin=input("Enter you Pin: ")
            if self.pin==enter_pin:
                print("Available Balance is: ",self.balance)
                return
            else:
                print("Your Pin is Wrong !!")
                attempts +=1
        print("Too many incorrect attempts. Account is in Sleep mode for 2 min !!")
        t.sleep(5)


    def withdrawl(self):
        attempts=0
        while attempts < 3:
            enter_pin=input("Enter you Pin: ")
            if self.pin==enter_pin:
                ammount=input("Enter Ammount for Withdraw: ")
                if ammount<=self.balance:
                    self.balance = self.balance - ammount
                    print(" Withdrawl Successfully. Your Available Balance is: ",self.balance)
                    return
                else:
                    print("Insufficient Balance !!")
            else:
                print("Your Pin is Wrong !!")
                attempts +=1
        print("Too many incorrect attempts. Account is in Sleep mode for 2 min !!")
        t.sleep(5)


    def menu(self):
        user_input=input('''
1.Pin create - Press:1
2.Pin change - Press:2
3.Check Balance - Press:3
4.Withdrawal - Press:4
5.Exit - Press:5 
'''
)

        if user_input =='1':
            # create pin 
            self.create_pin()
            self.menu()
        elif user_input =='2':
            # change pin 
            self.change_pin()
            self.menu()
        elif user_input =='3':
            # check balance
            self.check_balance()
            self.menu()
        elif user_input =='4':
            # withdrawl
            self.withdrawl()
            self.menu()
        elif user_input == '5':
            # exit
            print("\n")
            print("---- Exit Section ----")
            exit_choice = input("Do you want to exit the program? (yes/no): ").strip().lower()
            if exit_choice == 'yes':
                print("Wishing you a wonderful day ahead! 😊")
                print("Goodbye! 👋")    
            else:
                print("\n🔁 Taking you back to the main menu... Let's continue! 🚀\n")
                self.menu()

obj=Atm()