class Bank:
    def __init__(self,Name,Account_Number):
        self.name=Name
        self.account_number=Account_Number

class OtherDetails:
    def __init__(self,Balance,Code):
        self.Bank_balance=Balance
        self.IFSC_code=Code

class Child(Bank,OtherDetails):
    def __init__(self,Name,Account_Number,Balance,Code):

        Bank.__init__(self,Name,Account_Number)
        OtherDetails.__init__(self,Balance,Code)

        print("\nYour Nmae is: ",self.name)
        print("Your Account_Number is: ",self.account_number)
        print("Your Bank_Balnce is: ",self.Bank_balance)
        print("Your IFSC Code is: ",self.IFSC_code)

Name=input("Enter Your Name: ")
Account_Number=int(input("Enter Your Account_Number: "))
Balance=float(input("Enter your Balance: "))
Code=input("Enter Your IFSC Code: ")

c=Child(Name,Account_Number,Balance,Code)

