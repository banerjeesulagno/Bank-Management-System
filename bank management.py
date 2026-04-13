# Bank Management System

accounts = {}

MIN_BALANCE = 500
INTEREST_RATE = 0.075

def create_account():
    acc_no = input("Enter Account Number: ").strip()

    if not acc_no:
        print("Account number cannot be empty!")
        return
    if not acc_no.isdigit():
        print("Account number must contain only digits!")
        return
    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter Name: ")

    print("Select Account Type:")
    print("1. Savings")
    print("2. Current")
    acc_type_choice = input("Enter choice: ")

    if acc_type_choice == '1':
        acc_type = "Savings"
    elif acc_type_choice == '2':
        acc_type = "Current"
    else:
        print("Invalid account type!")
        return

    balance = float(input("Enter Initial Deposit: "))

    if balance < MIN_BALANCE:
        print(f"Minimum balance should be {MIN_BALANCE}!")
        return

    accounts[acc_no] = {
        "name": name,
        "balance": balance,
        "type": acc_type
    }

    print("Account Created Successfully!")


def deposit():
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter Amount to Deposit: "))
    accounts[acc_no]["balance"] += amount

    print("Deposit Successful!")


def withdraw():
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter Amount to Withdraw: "))

    current_balance = accounts[acc_no]["balance"]

    if current_balance - amount < MIN_BALANCE:
        print(f"Cannot withdraw! Minimum balance of {MIN_BALANCE} must be maintained.")
    else:
        accounts[acc_no]["balance"] -= amount
        print("Withdrawal Successful!")


def check_balance():
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    acc = accounts[acc_no]

    print(f"Account Holder: {acc['name']}")
    print(f"Account Type: {acc['type']}")
    print(f"Balance: {acc['balance']}")


def display_all_accounts():
    if not accounts:
        print("No accounts available.")
        return

    print("All Accounts:")
    for acc_no, details in accounts.items():
        print(f"Acc No: {acc_no}, Name: {details['name']}, Type: {details['type']}, Balance: {details['balance']}")


def calculate_interest():
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    acc = accounts[acc_no]

    if acc["type"] == "Savings":
        interest = acc["balance"] * INTEREST_RATE
        print(f"Interest (7.5%): {interest}")
    else:
        print("Interest is only applicable for Savings Account.")


while True:
    print("\n---- Bank Management System ----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Calculate Interest")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        display_all_accounts()
    elif choice == '6':
        calculate_interest()
    elif choice == '7':
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Please try again.")