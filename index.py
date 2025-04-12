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
    pass
# calculataing total expenses
def total_expense():
    pass
#Save expenses in file
def save_expenses():
    pass
#load in file
def load():
    pass
def main():
    
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
            total_expense
        elif choice == "4":
            save_expenses()
            print("Save successfully !!")
        elif choice == "5":
            break
        else:
            print("Enter a valid choice !!?")

if __name__ == "__main__":
    main()
