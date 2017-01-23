class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance -= amount
            return self.balance
