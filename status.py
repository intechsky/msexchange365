import json
import random
import re
import os
from datetime import datetime

DATA_FILE = "system_data.json"


# =============================
# DATA HANDLING
# =============================

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "expenses": [], "library": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


data = load_data()


# =============================
# USER SYSTEM
# =============================

def register():
    username = input("Create username: ")
    password = input("Create password: ")

    if username in data["users"]:
        print("❌ Username already exists.")
        return

    data["users"][username] = password
    save_data(data)
    print("✅ Registration successful.")


def login():
    username = input("Username: ")
    password = input("Password: ")

    if data["users"].get(username) == password:
        print("🎉 Login successful.")
        return True
    else:
        print("❌ Invalid credentials.")
        return False


# =============================
# EXPENSE TRACKER
# =============================

def add_expense():
    name = input("Expense name: ")
    category = input("Category: ")
    amount = float(input("Amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": date
    }

    data["expenses"].append(expense)
    save_data(data)
    print("✅ Expense added.")


def view_expenses():
    total = 0
    print("\n--- Expenses ---")
    for e in data["expenses"]:
        print(f"{e['date']} | {e['name']} ({e['category']}) - ${e['amount']}")
        total += e["amount"]

    print("Total Spent:", total)


# =============================
# LIBRARY SYSTEM
# =============================

def add_book():
    title = input("Book title: ")
    author = input("Author: ")

    if title in data["library"]:
        print("Book already exists.")
        return

    data["library"][title] = {"author": author, "borrowed": False}
    save_data(data)
    print("Book added.")


def borrow_book():
    title = input("Book title: ")

    if title in data["library"] and not data["library"][title]["borrowed"]:
        data["library"][title]["borrowed"] = True
        save_data(data)
        print("Book borrowed.")
    else:
        print("Book not available.")


def return_book():
    title = input("Book title: ")

    if title in data["library"] and data["library"][title]["borrowed"]:
        data["library"][title]["borrowed"] = False
        save_data(data)
        print("Book returned.")
    else:
        print("Book not borrowed.")


def list_books():
    print("\n--- Library ---")
    for title, info in data["library"].items():
        status = "Borrowed" if info["borrowed"] else "Available"
        print(f"{title} by {info['author']} - {status}")


# =============================
# DICE GAME
# =============================

def roll_dice():
    rolls = [random.randint(1, 6) for _ in range(3)]
    print("🎲 Rolls:", rolls, "Total:", sum(rolls))


# =============================
# EMAIL VALIDATION
# =============================

def validate_email():
    email = input("Enter email: ")
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if re.match(pattern, email):
        print("✅ Valid email")
    else:
        print("❌ Invalid email")


# =============================
# MAIN SYSTEM MENU
# =============================

def main_menu():
    while True:
        print("\n===== SYSTEM MENU =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Add Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. List Books")
        print("7. Roll Dice")
        print("8. Validate Email")
        print("9. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            add_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            list_books()
        elif choice == "7":
            roll_dice()
        elif choice == "8":
            validate_email()
        elif choice == "9":
            break
        else:
            print("Invalid option.")


# =============================
# START PROGRAM
# =============================

while True:
    print("\n===== LOGIN MENU =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    option = input("Choose: ")

    if option == "1":
        register()
    elif option == "2":
        if login():
            main_menu()
    elif option == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
