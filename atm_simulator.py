import json
import os

FILE_NAME = "account.json"


def load_account():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return {
        "name": "Mimi",
        "pin": "1234",
        "balance": 10000,
        "transactions": []
    }


def save_account(account):
    with open(FILE_NAME, "w") as file:
        json.dump(account, file, indent=4)


def verify_pin(account):
    attempts = 3

    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")

        if pin == account["pin"]:
            print("\nLogin successful!")
            return True

        attempts -= 1
        print(f"Incorrect PIN. Attempts remaining: {attempts}")

    print("\nToo many incorrect attempts. Access denied.")
    return False


def check_balance(account):
    print("\n========== BALANCE ==========")
    print(f"Available Balance: ₹{account['balance']:.2f}")


def deposit(account):
    try:
        amount = float(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("Enter a valid amount.")
            return

        account["balance"] += amount

        account["transactions"].append(
            f"Deposited ₹{amount:.2f}"
        )

        save_account(account)

        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New Balance: ₹{account['balance']:.2f}")

    except ValueError:
        print("Please enter a valid amount.")


def withdraw(account):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Enter a valid amount.")
            return

        if amount > account["balance"]:
            print("Insufficient balance!")
            return

        account["balance"] -= amount

        account["transactions"].append(
            f"Withdrawn ₹{amount:.2f}"
        )

        save_account(account)

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Remaining Balance: ₹{account['balance']:.2f}")

    except ValueError:
        print("Please enter a valid amount.")


def change_pin(account):
    old_pin = input("Enter current PIN: ")

    if old_pin != account["pin"]:
        print("Incorrect current PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    confirm_pin = input("Confirm new PIN: ")

    if new_pin != confirm_pin:
        print("PINs do not match.")
        return

    account["pin"] = new_pin
    save_account(account)

    print("PIN changed successfully!")


def mini_statement(account):
    print("\n========== MINI STATEMENT ==========")

    if not account["transactions"]:
        print("No transactions yet.")
        return

    for number, transaction in enumerate(
        account["transactions"][-5:], 1
    ):
        print(f"{number}. {transaction}")

    print("------------------------------------")
    print(f"Current Balance: ₹{account['balance']:.2f}")


def main():
    account = load_account()

    print("=" * 40)
    print("        WELCOME TO PYTHON ATM")
    print("=" * 40)

    if not verify_pin(account):
        return

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            check_balance(account)

        elif choice == "2":
            deposit(account)

        elif choice == "3":
            withdraw(account)

        elif choice == "4":
            change_pin(account)

        elif choice == "5":
            mini_statement(account)

        elif choice == "6":
            print("\nThank you for using Python ATM!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()