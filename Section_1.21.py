class BankAccount:
    total_accounts = 0  # Class-level variable to track total accounts

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Instance-level data
        self.balance = balance  # Instance-level data
        BankAccount.total_accounts += 1  # Increment the total count of accounts

    # Instance method: used to access instance-specific data
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} deposited. New balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn. Remaining balance: {self.balance}"
        else:
            return "Insufficient funds."

    # Class method: used to interact with class-level data or create new instances
    @classmethod
    def create_account(cls, account_holder, initial_deposit=0):
        return cls(account_holder, initial_deposit)

    # Static method: utility function that does not depend on instance or class-level data
    @staticmethod
    def is_valid_account_number(account_number):
        # Static method that checks if an account number is valid (for simplicity, assume it must be a positive integer)
        return isinstance(account_number, int) and account_number > 0

# Creating some accounts using the class method
account1 = BankAccount.create_account("Alice", 500)
account2 = BankAccount.create_account("Bob", 1000)

# Using instance methods to deposit and withdraw money
print(account1.deposit(200))  # Output: 200 deposited. New balance: 700
print(account2.withdraw(500))  # Output: 500 withdrawn. Remaining balance: 500

# Using class method to get the total number of accounts
print(BankAccount.total_accounts)  # Output: 2

# Using static method to check account number validity
print(BankAccount.is_valid_account_number(123456))  # Output: True
print(BankAccount.is_valid_account_number("abc123"))  # Output: False
