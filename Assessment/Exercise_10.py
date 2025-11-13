#EX 10

# OOP – Encapsulation and Methods

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance      

    def deposit(self, amount):
        self.__balance += amount              

    def withdraw(self, amount):
        if amount <= self.__balance:           
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance 


acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)

print("Current Balance:", acc.get_balance())


"""

BankAccount uses a private balance attribute.

deposit() adds money.

withdraw() removes money but prevents negative balance.

get_balance() returns the current balance.

"""