
class BankAccount:
    """
    A base class for all bank accounts. It handles basic functionalities
    like deposits, withdrawals, and checking the balance.
    """
    def __init__(self, account_holder_name, initial_balance=0):
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        """Adds funds to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws funds from the account."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def get_balance(self):
        """Returns the current account balance."""
        return self.balance

    def get_info(self):
        """Prints a summary of the account."""
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Current Balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    """
    A subclass of BankAccount for savings. It includes an interest rate.
    """
    def __init__(self, account_holder_name, initial_balance=0, interest_rate=0.01):
        super().__init__(account_holder_name, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Applies interest to the balance."""
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        print(f"Interest of ${interest_earned:.2f} applied. New balance is ${self.balance:.2f}.")
    
    def get_info(self):
        """Overrides the parent method to include interest rate information."""
        super().get_info()
        print(f"Interest Rate: {self.interest_rate * 100:.2f}%")


class CheckingAccount(BankAccount):
    """
    A subclass of BankAccount for checking. It allows for an overdraft limit.
    """
    def __init__(self, account_holder_name, initial_balance=0, overdraft_limit=100):
        super().__init__(account_holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Overrides the parent method to allow for overdrafts."""
        if amount > 0:
            if self.balance - amount >= -self.overdraft_limit:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
                return True
            else:
                print("Overdraft limit exceeded.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def get_info(self):
        """Overrides the parent method to include overdraft limit information."""
        super().get_info()
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")



print("--- Creating Accounts ---")
savings = SavingsAccount("Alice", initial_balance=500)
checking = CheckingAccount("Bob", initial_balance=200, overdraft_limit=50)

print("\n--- Savings Account Activity ---")
savings.get_info()
savings.deposit(150)
savings.withdraw(50)
savings.apply_interest()

print("\n--- Checking Account Activity ---")
checking.get_info()
checking.deposit(300)
checking.withdraw(250)
checking.withdraw(300) 
checking.withdraw(100)

print("\n--- Final Account Status ---")
savings.get_info()
checking.get_info()
