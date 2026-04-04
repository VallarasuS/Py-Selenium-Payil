# Account
#   - account_number = "AC123"
#   - balance = 1000

#   - deposit(100)
#   - withdraw(500)
#   - check_balance() -> 1100, 600



class Account:

    def __init__(self, balance, account_number):
        self.balance = balance
        self._locker = "Secret"

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def check_balance(self):
        print(self.balance)


my_account = Account(1000, "ABC123")
my_account.check_balance()

another_account = Account(2000, "ABC321")
another_account.check_balance()