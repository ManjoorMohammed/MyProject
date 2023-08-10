class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

accounts = {} 

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1: Account Creation")
        print("2: Login")
        print("3: Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            Name = input("Enter Your Name: ")
            age = input("Enter Your age: ")
            Mobile = input("Enter Your 10 Digit mobile Number: ")
            account_number = Mobile[:6:]+"0000"+age
            password = input("Password: ")
            accounts[account_number] = {'password': password, 'account': BankAccount()}
            print("Congtratulations!! Your Account created with Account Number: ",account_number)

        elif choice == 2:
            account_number = input("Enter Account Number: ")
            password = input("Enter Password: ")
            if account_number in accounts and accounts[account_number]['password'] == password:
                login_menu(accounts[account_number]['account'])
            else:
                print("Invalid account number or password.")

        elif choice == 3:
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

def login_menu(account):
    while True:
        print("\nLogin Menu:")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Check Balance")
        print("4: Logout")

        choice = int(input("Select an option: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print("Deposit successful. New balance:", account.balance)

        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= account.balance:
                account.withdraw(amount)
                print("Withdrawal successful. New balance:", account.balance)
            else:
                print("Insufficient balance.")

        elif choice == 3:
            print("Current balance:", account.balance)

        elif choice == 4:
            print("Logging out.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
