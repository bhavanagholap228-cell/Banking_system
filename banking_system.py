"""
BANKING SYSTEM - Menu Driven Mini Project
------------------------------------------
A simple Python based banking system that simulates basic banking
operations using variables, loops, conditional statements,
lists/dictionaries and modules (random, datetime).

Features:
1. Account Creation (name, phone number, PIN)
2. Secure Login (account number + PIN)
3. Check Balance
4. Deposit Money
5. Withdraw Money
6. Transfer Funds
7. View Transaction History
8. Change PIN
9. Logout
"""

import random
import datetime

# ---------------------------------------------------------------
# GLOBAL DATA STORE
# accounts = dictionary of dictionaries
# key   -> account number (int)
# value -> {name, phone, pin, balance, transactions}
# ---------------------------------------------------------------
accounts = {}


# ---------------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------------
def generate_account_number():
    """Generate a unique 6 digit account number using random module."""
    while True:
        acc_no = random.randint(100000, 999999)
        if acc_no not in accounts:
            return acc_no


def get_current_time():
    """Return current date & time as a formatted string using datetime module."""
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


def add_transaction(acc_no, description):
    """Add a transaction entry to the account's transaction history list."""
    timestamp = get_current_time()
    entry = f"[{timestamp}] {description}"
    accounts[acc_no]["transactions"].append(entry)


def is_valid_amount(amount):
    """Basic validation for deposit/withdraw/transfer amounts."""
    return amount > 0


# ---------------------------------------------------------------
# CORE BANKING FEATURES
# ---------------------------------------------------------------
def create_account():
    print("\n----- CREATE NEW ACCOUNT -----")
    name = input("Enter your full name: ").strip()
    phone = input("Enter your phone number: ").strip()

    while True:
        pin = input("Set a 4-digit security PIN: ").strip()
        if pin.isdigit() and len(pin) == 4:
            break
        print("Invalid PIN. PIN must be exactly 4 digits.")

    acc_no = generate_account_number()

    accounts[acc_no] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    add_transaction(acc_no, "Account created")

    print("\nAccount created successfully!")
    print(f"Your Account Number is: {acc_no}")
    print("Please note this down. You will need it to login.")


def login():
    print("\n----- LOGIN -----")
    try:
        acc_no = int(input("Enter your account number: ").strip())
    except ValueError:
        print("Invalid account number format.")
        return None

    if acc_no not in accounts:
        print("Account not found.")
        return None

    pin = input("Enter your PIN: ").strip()
    attempts = 3

    while attempts > 0:
        if pin == accounts[acc_no]["pin"]:
            print(f"\nLogin successful. Welcome, {accounts[acc_no]['name']}!")
            return acc_no
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")
            if attempts > 0:
                pin = input("Enter your PIN: ").strip()

    print("Too many incorrect attempts. Login failed.")
    return None


def check_balance(acc_no):
    print("\n----- ACCOUNT BALANCE -----")
    print(f"Account Holder : {accounts[acc_no]['name']}")
    print(f"Account Number : {acc_no}")
    print(f"Balance        : Rs. {accounts[acc_no]['balance']}")


def deposit_money(acc_no):
    print("\n----- DEPOSIT MONEY -----")
    try:
        amount = float(input("Enter amount to deposit: Rs. "))
    except ValueError:
        print("Invalid amount entered.")
        return

    if not is_valid_amount(amount):
        print("Deposit amount must be greater than zero.")
        return

    accounts[acc_no]["balance"] += amount
    add_transaction(acc_no, f"Deposited Rs. {amount}")
    print(f"Rs. {amount} deposited successfully.")
    print(f"New Balance: Rs. {accounts[acc_no]['balance']}")


def withdraw_money(acc_no):
    print("\n----- WITHDRAW MONEY -----")
    try:
        amount = float(input("Enter amount to withdraw: Rs. "))
    except ValueError:
        print("Invalid amount entered.")
        return

    if not is_valid_amount(amount):
        print("Withdrawal amount must be greater than zero.")
        return

    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance.")
        return

    accounts[acc_no]["balance"] -= amount
    add_transaction(acc_no, f"Withdrew Rs. {amount}")
    print(f"Rs. {amount} withdrawn successfully.")
    print(f"New Balance: Rs. {accounts[acc_no]['balance']}")


def transfer_funds(acc_no):
    print("\n----- TRANSFER FUNDS -----")
    try:
        receiver_acc = int(input("Enter receiver's account number: "))
    except ValueError:
        print("Invalid account number format.")
        return

    if receiver_acc not in accounts:
        print("Receiver account not found.")
        return

    if receiver_acc == acc_no:
        print("You cannot transfer funds to your own account.")
        return

    try:
        amount = float(input("Enter amount to transfer: Rs. "))
    except ValueError:
        print("Invalid amount entered.")
        return

    if not is_valid_amount(amount):
        print("Transfer amount must be greater than zero.")
        return

    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance.")
        return

    # Deduct from sender
    accounts[acc_no]["balance"] -= amount
    add_transaction(acc_no, f"Transferred Rs. {amount} to Account {receiver_acc}")

    # Add to receiver
    accounts[receiver_acc]["balance"] += amount
    add_transaction(receiver_acc, f"Received Rs. {amount} from Account {acc_no}")

    print(f"Rs. {amount} transferred successfully to Account {receiver_acc}.")
    print(f"New Balance: Rs. {accounts[acc_no]['balance']}")


def view_transaction_history(acc_no):
    print("\n----- TRANSACTION HISTORY -----")
    transactions = accounts[acc_no]["transactions"]

    if len(transactions) == 0:
        print("No transactions found.")
        return

    for i in range(len(transactions)):
        print(f"{i + 1}. {transactions[i]}")


def change_pin(acc_no):
    print("\n----- CHANGE PIN -----")
    old_pin = input("Enter current PIN: ").strip()

    if old_pin != accounts[acc_no]["pin"]:
        print("Incorrect current PIN.")
        return

    while True:
        new_pin = input("Enter new 4-digit PIN: ").strip()
        if new_pin.isdigit() and len(new_pin) == 4:
            break
        print("Invalid PIN. PIN must be exactly 4 digits.")

    confirm_pin = input("Confirm new PIN: ").strip()

    if new_pin != confirm_pin:
        print("PINs do not match. PIN change cancelled.")
        return

    accounts[acc_no]["pin"] = new_pin
    add_transaction(acc_no, "PIN changed")
    print("PIN changed successfully.")


# ---------------------------------------------------------------
# MENUS
# ---------------------------------------------------------------
def account_menu(acc_no):
    """Menu shown after a successful login."""
    while True:
        print("\n========== ACCOUNT MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Funds")
        print("5. View Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("===================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            check_balance(acc_no)
        elif choice == "2":
            deposit_money(acc_no)
        elif choice == "3":
            withdraw_money(acc_no)
        elif choice == "4":
            transfer_funds(acc_no)
        elif choice == "5":
            view_transaction_history(acc_no)
        elif choice == "6":
            change_pin(acc_no)
        elif choice == "7":
            print("Logging out...")
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 7.")


def main_menu():
    """Main entry menu of the application."""
    while True:
        print("\n============================================")
        print("        WELCOME TO PYTHON BANKING SYSTEM")
        print("============================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("============================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            logged_in_acc = login()
            if logged_in_acc is not None:
                account_menu(logged_in_acc)
        elif choice == "3":
            print("\nThank you for using Python Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 3.")


# ---------------------------------------------------------------
# PROGRAM ENTRY POINT
# ---------------------------------------------------------------
if __name__ == "__main__":
    main_menu()
