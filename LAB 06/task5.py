# BankAccount class definition
class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize account with an optional initial balance
        self._balance = initial_balance

    def deposit(self, amount):
        # Add amount to the balance if amount is positive
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Subtract amount from balance if sufficient funds exist
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def balance(self):
        # Return the current balance
        return self._balance

# Main program to interact with the user
def main():
    # Create a bank account with zero initial balance
    account = BankAccount()

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current balance: ${account.balance()}")
        elif choice == '4':
            print("Thank you for using the bank account system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
