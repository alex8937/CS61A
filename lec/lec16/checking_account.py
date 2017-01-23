from account import *

class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> ch = CheckingAccount('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

class SavingAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1


class Bank:
    """A bank has accounts and pays interest.

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> jack.interest
    0.01
    >>> john.interest = 0.06
    >>> bank.pay_interest()
    >>> john.balance
    10.6
    >>> jack.balance
    5.05
    """
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, account_type = Account):
        account = account_type(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for account in self.accounts:
            account.deposit(account.interest * account.balance)
