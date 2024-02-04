class Account:

    def __init__(self, owner: str = "Unknow", balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float, logging: bool = False):
        if amount <= 0:
            if logging:
                print("Deposit rejected!")
                print("Reason: Negative deposit amount.")

            return

        self.balance += amount

        if logging:
            print("Withdraw approved!")
            print(f"{self.owner} balance: {self.balance}")

    def withdraw(self, amount: float, logging: bool = False):
        if amount <= 0:
            if logging:
                print("Withdrawal rejected!")
                print("Reason: Negative Withdrawal amount.")

            return
        
        if amount > self.balance:
            if logging:
                print("Withdrawal rejected!")
                print("Withdrawals may not exceed the available balance.")

            return

        self.balance -= amount

        if logging:
            print("Withdraw approved!")
            print(f"{self.owner} balance: {self.balance}")


steve = Account("Steven", 200)

steve.deposit(15, True)
steve.deposit(-10, True)
steve.deposit(0, True)

steve.withdraw(100, True)
steve.withdraw(-20, True)
steve.withdraw(0, True)
steve.withdraw(1000, True)