# Parent class representing a generic bank account
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        # Public attribute: can be accessed from anywhere
        self.account_number = account_number

        # Protected attribute: intended to be accessed only within the class and its subclasses
        self._holder_name = holder_name

        # Private attribute: accessible only within this class (name mangled to _BankAccount__balance)
        self.__balance = balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposit, current balance is {self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    # Public method to retrieve current balance
    def get_balance(self):
        return self.__balance

    # Protected method to display account holder's name
    def _display_holder(self):
        print(f"Account Holder : {self._holder_name}")


# Subclass that represents a savings account, inherits from BankAccount
class SavingAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        # Call parent constructor using super()
        super().__init__(account_number, holder_name, balance)

        # Additional attribute specific to SavingAccount
        self.interest_rate = interest_rate

    # Method to apply interest to the current balance
    def apply_interest(self):
        # Calculate interest based on current balance and interest rate
        interest = self.get_balance() * (self.interest_rate / 100)
        print(f"Applying interest: ₹{interest}")
        
        # Add the calculated interest to the account balance using deposit method
        self.deposit(interest)

    # Method to display detailed information about the savings account
    def display_info(self):
        self._display_holder()  # Calling protected method from parent class
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.get_balance()}")
        print(f"Interest Rate: {self.interest_rate}%")


# Create an object of SavingAccount with sample data
acc = SavingAccount("1234567890", "Himanshu", 550000, 4.5)

# Display account info (holder name, account number, balance, interest rate)
acc.display_info()

# Deposit ₹5000 into the account
acc.deposit(5000)

# Withdraw ₹3000 from the account
acc.withdraw(3000)

# Apply interest based on current balance and interest rate
acc.apply_interest()
