class Account:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Yetersiz bakiye!")

class SavingAccount(Account):
    def __init__(self, account_holder, balance = 0, interest_rate = 0):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        faiz_geliri = self.balance * self.interest_rate
        self.balance += faiz_geliri

class CheckingAccount(Account):
    def __init__(self, account_holder, balance = 0, overdraft_limit = 0):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Para çekilemedi!")
        else:
           self.balance -= amount

