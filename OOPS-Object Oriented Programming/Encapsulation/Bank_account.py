class BankAccount:
    def __init__ (self, owner, balance):
        self. owner = owner
        self.__balance = balance # private variable
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
acc = BankAccount ("John", 1000)
acc.deposit (500)
print("The Balance of your account is: ",acc.get_balance())  # 1500
print()
# print(acc._BankAccount__balance)  ## Way to access the Private Member
print(acc.__balance)  # Error (private)