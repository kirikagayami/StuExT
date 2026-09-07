option = 0
expenses = []
while option != 4:
    print("=== StuExT ===")
    print()
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Show statistics")
    print("4. Exit")
    print()
    option = int(input("Choose an option: "))
    print()
    
    if option == 1:
        description = input("Enter description: ")
        amount = int(input("Enter expense: "))
        while amount <= 0:
            print("Please input the valid price.")
            amount = int(input("Enter expense: "))
            
        expense = [description, amount]
    
        expenses.append(expense)
        print()
    
    # if len(expenses) == 0:
    #         print ("No data available.")
    # else:
    if option == 2:
        if len(expenses) == 0:
            print("No data available.")
        else:
            for i in range(len(expenses)):
                print("Item no ", i+1, ": ", expenses[i][0])
                print("Item Price: ", expenses[i][1])
                print()
    if option == 3:
        if len(expenses) == 0:
            print("No data available.")
        else:
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
            average = total/len(expenses)
            print("Average Spent: ", average)
            print()
print("Goodbye...")