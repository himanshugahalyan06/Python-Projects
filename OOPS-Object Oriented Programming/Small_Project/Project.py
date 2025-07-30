## Project Objective:
## Build a system to simulate an online payment gateway that can handle payments via Credit Card, Debit Card, and UPI using Abstraction and Polymorphism in Python.
## Step 1: Import ABC module for abstraction
## Step 2: Create an abstract base class
## Step 3: Create concrete classes for each payment type
## Step 4: Create a function to make a payment
## Step 5: Simulate payments
from abc import ABC, abstractmethod

# Abstract base class
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete classes for each payment type
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"✅ Payment of ₹{amount} done using Credit Card.")

class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"✅ Payment of ₹{amount} done using Debit Card.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"✅ Payment of ₹{amount} done using UPI.")

# Function to process the payment
def make_payment(method: PaymentMethod, amount: float):
    method.pay(amount)

# Main function with user choice and exit option
def main():
    while True:
        print("\n=== Online Payment Gateway ===")
        print("Choose Payment Method:")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. UPI")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '4':
            print("👋 Thank you for using the payment gateway. Goodbye!")
            break

        try:
            amount = float(input("Enter the amount to pay: ₹"))
            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue
        except ValueError:
            print("❌ Invalid amount! Please enter a numeric value.")
            continue

        if choice == '1':
            method = CreditCard()
        elif choice == '2':
            method = DebitCard()
        elif choice == '3':
            method = UPI()
        else:
            print("❌ Invalid choice! Please select 1, 2, 3, or 4.")
            continue

        make_payment(method, amount)

# Run the program
if __name__ == "__main__":
    main()