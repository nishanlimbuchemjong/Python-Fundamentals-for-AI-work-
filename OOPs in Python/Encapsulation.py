"""
Encapsulation in Python:
    Encapsulation is one of the fundamental concepts of object-oriented programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit known as a class. Moreover, encapsulation is often used to restrict access to certain details of an object, hiding the internal workings and only exposing a controlled interface.

    In Python, encapsulation is implemented using private and public access modifiers:
        - Public attributes and methods can be accessed from outside the class.
        - Private attributes and methods are restricted from being accessed directly from outside the class.
"""
# For Example:
    # A very simple example of encapsulation in Python using a class with both public and private attributes:

class Account:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder    # Public attribute
        self.__balance = balance        # Private attribute (encapsulated)

    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            print(f"Deposited amount = RS. {amount}\nCurrent balance = RS. {self.__balance}")
        else:
            print("Deposited amount should be positive")
        
    def withdrawl(self, amount):
        if amount < self.__balance :
            self.__balance -= amount
            print(f"Withdrawl amount = RS. {amount}\nCurrent balance = RS. {self.__balance}")
        else:
            print("Insufficient balance")
            
    def get_balance(self):
        return self.__balance

# Create a Account object
acc = Account("Nishan Limbu", 10000000)

print("\nDeposited:")
acc.deposit(50000)

print("\nWithdrawl:")
acc.withdrawl(45)

print("\nTotal Balance::")
print(f"Final Balance = {acc.get_balance()}")

"""
Output:

Deposited:
Deposited amount = RS. 50000
Current balance = RS. 10050000

Withdrawl:
Withdrawl amount = RS. 45
Current balance = RS. 10049955

Total Balance::
Final Balance = 10049955

"""