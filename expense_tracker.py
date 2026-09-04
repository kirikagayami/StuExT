num_expenses = int(input("Enter how many expense(s): "))
if num_expenses == 0:
    print("Expense(s) cannot be zero.")
elif num_expenses < 0:
    print("Expense(s) cannot be negative")
else:
    expenses = []
# Loop Through the expense list to register a new expense based on num_expense variable
    for i in range(num_expenses):
        description = input("Enter description: ")
        amount = int(input("Enter expense: "))
        while amount <= 0:
            print("Please input the valid price.")
            amount = int(input("Enter expense: "))

        expense = [description, amount]
        expenses.append(expense)

# Loop through the expenses to acquire number of item
    for i in range(num_expenses):
        print("Item no ", i+1, ": ", expenses[i][0])
        print("Item Price: ", expenses[i][1])

    total = 0
    for expense in expenses:
        total += expense[1]
        
    maximum = 0
    max_desc = ""
    minimum = expenses[0][1]
    min_desc = expenses[0][0]
    for expense in expenses:
        if expense[1] > maximum:
            maximum = expense[1]
            max_desc = expense[0]
        
        if expense[1] < minimum:
            minimum = expense[1]
            min_desc = expense[0]




    print("Total:", total)
    print("Most Pricy Item: ", max_desc, " Price : ", maximum)
    print("Cheapest Item: ", min_desc, " Price : ", minimum)
    average = total/num_expenses
    print("Average Spent: ", average)
