# BankAccount

class BankAccount:
    def __init__(self, balance=0) -> None:
        self._balance = balance

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("На счете недостаточно средств")

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)