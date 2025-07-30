from abc import ABC ,abstractmethod ## always import this in your code 
class BankApp(ABC): ## Abstract Class

    def database(self):
        print("Connected to Database !!")

    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def display(slef):
        pass

class MobileApp(BankApp):
    def mobile_login(self):
        print("Login Into Moblie !!")

    def security(self): ## override the sequrity method 
        print("Mobile Security !!")
## we cannot make object of Abstract class 
    def display(slef):
        print("Display !!")

mb=MobileApp()
mb.security()
mb.display()
