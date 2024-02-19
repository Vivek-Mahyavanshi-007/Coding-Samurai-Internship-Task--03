import os
import json
from datetime import datetime

# Add colorama module for colorful text

import colorama
from colorama import Fore, Back, Style

# Initialize colors
colorama.init(autoreset=True)

# Function to load expense data from file

def load_expense_data(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            print(Fore.RED + f"Error: Unable to parse JSON data in '{filename}'. Creating new empty list of expenses.")
            return []
    else:
        print(Fore.YELLOW + f"Warning: File '{filename}' not found. Creating new empty list of expenses.")
        return []

# Function to save expense data to file

def save_expense_data(filename, expenses):
    with open(filename, "w") as file:
        json.dump(expenses, file)

# Function to add an expense

def add_expense(expenses):
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")
    description = input("Enter a brief description: ")
    date = datetime.now().strftime("%Y-%m-%d")
    expenses.append({"date": date, "amount": amount, "category": category, "description": description})
    print(Fore.GREEN + "Expense added successfully!")

# Function to list all expenses

def list_expenses(expenses):
    if not expenses:
        print(Fore.YELLOW + "No expenses recorded!")
    else:
        for expense in expenses:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

# Function to calculate total expenses for a specified time frame

def calculate_total_expenses(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(Fore.CYAN + f"Total expenses: {total}")

# Function to generate and display a monthly report

def generate_monthly_report(expenses):
    monthly_report = {}
    for expense in expenses:
        month = expense['date'][:7] # Extracting year and month (YYYY-MM)
        if month not in monthly_report:
            monthly_report[month] = 0
        monthly_report[month] += expense['amount']
    print(Fore.MAGENTA + "Monthly Report:")
    for month, total in monthly_report.items():
        print(f"{month}: {total}")

# Main function

def main():
    filename = "Output_Tasks.txt"
    expenses = load_expense_data(filename)

    while True:
        print(Fore.BLUE + "\nExpense Tracker")
        print(Fore.CYAN + "_" * 50)
        print("\n1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Generate Monthly Report")
        print("5. Exit\n")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            calculate_total_expenses(expenses)
        elif choice == "4":
            generate_monthly_report(expenses)
        elif choice == "5":
            save_expense_data(filename, expenses)
            print(Fore.GREEN + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
