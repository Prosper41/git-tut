class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Example usage
account1 = BankAccount("1234567890", 1000)
print(f"Account Number: {account1.account_number}")
print(f"Current Balance: ${account1.balance}")

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)
