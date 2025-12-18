"""
Expense Tracker Project
Author: <Your Name>
Description:
A simple Python program to record expenses from multiple users,
categorize them, and calculate total spending.
Credit:
Portions of the logic structure and commenting guidance were supported
using ChatGPT prompts.
"""


# -----------------------------
# Function: add_expense
# Purpose: Takes user input and stores expense data as a dictionary
# -----------------------------
def add_expense(expense_list):
    name = input("\nEnter user name: ")
    category = input("\nEnter expense category (Food/Travel/Shopping/Other): ")
    amount = float(input("\nEnter amount spent: "))

    # Store expense in dictionary
    expense = {"name": name, "category": category, "amount": amount}

    expense_list.append(expense)
    print("\nExpense added successfully!\n")


# -----------------------------
# Function: total_expense
# Purpose: Calculates the total amount spent
# -----------------------------
def total_expense(expense_list):
    total = 0
    for expense in expense_list:  # loop used
        total += expense["amount"]
    return total


# -----------------------------
# Function: category_summary
# Purpose: Shows total expenses grouped by category
# -----------------------------
def category_summary(expense_list):
    summary = {}
    for expense in expense_list:
        category = expense["category"]
        amount = expense["amount"]

        # conditional used
        if category not in summary:
            summary[category] = amount
        else:
            summary[category] += amount

    return summary


# -----------------------------
# Main Program
# -----------------------------
expenses = []  # List of dictionaries storing all expenses

print("========== Welcome to Expense Tracker ==========\n")

while True:
    print("Choose an option:")
    print("1. Add new expense")
    print("2. View total expenses")
    print("3. View category-wise summary")
    print("4. Exit")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        total = total_expense(expenses)
        print(f"\nTotal money spent: ₹{total}\n")

    elif choice == "3":
        summary = category_summary(expenses)
        print("\nCategory-wise Expense Summary:")
        for category, amount in summary.items():
            print(f"{category}: ₹{amount}")
        print()

    elif choice == "4":
        print("\nThank you for using the tracker!")
        break

    else:
        print("\nInvalid choice. Try again.\n")
