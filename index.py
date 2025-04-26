import json

#Constructor
class Expense:
    def __init__(self, description,amount,category):
        self.description = description
        self.amount = amount
        self.category = category

#Empty list
expenses = []
# Add expenses
def add_expense(description,amount,category):
    expense = Expense(description,amount,category)
    expenses.append(expense)

    
# for view expenses
def view_expense():
    if not expenses:
        print("No expenses found.")
        return
    for i, expense in enumerate(expenses, start=1):
        print("-------------------------")
        print(f"Expense {i}:")
        print(f"Description: {expense.description}")
        print(f"Amount: {expense.amount}")
        print(f"Category: {expense.category}")
        print("-------------------------")

# calculataing total expenses
def total_expense():
    total = 0
    for expense in expenses:
        total += expense.amount
    print(f"Total expenses: Rs.{total:.2f}")  

#Save expenses in file
def save_expenses():
    with open("expenses.json", "w") as file:
        data = [{"description": expense.description, "amount": expense.amount, "category": expense.category} for expense in expenses]
        json.dump(data, file)
#load in file
def load():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)
            for item in data:
                expense = Expense(item["description"], item["amount"], item["category"])
                expenses.append(expense)
    except FileNotFoundError:
        print("No previous data found.")

def main():
    load() # Load previous data
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Save Expenses")
        print("5. Exit")
        choice = input("Enter your option :")

        if choice == "1":
            description = input("Enter the description: ")
            amount = float(input("Enter the amount : "))
            category = input("Enter the category here :")
            add_expense(description,amount,category)
            print("Data entry completd")
        elif choice == "2":
            view_expense()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            save_expenses()
            print("Save successfully !!")
        elif choice == "5":
            break
        else:
            print("Enter a valid choice !!?")

if __name__ == "__main__":
    main()
