# Expense Tracker - Project 2 

print("Welcome to the Expense Tracker!")
print("Enter your expenses one by one.")
print("Type 'quit' when you are done.\n")

total = 0  # Initialize accumulator

while True:
    try:
        expense = input("Enter expense amount (or type 'quit' to stop): ")
        if expense.lower() == "quit":   # Kill switch
            break
        total += int(expense)           # Accumulator pattern
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"\nFinal Total Spent: ${total:.2f}")