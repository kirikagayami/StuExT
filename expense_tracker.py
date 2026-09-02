expenses = []

num_expenses = int(input("Enter how many expense(s): "))

for i in range(num_expenses):
    description = input("Enter description: ")
    amount = int(input("Enter expense: "))

    expense = [description, amount]
    expenses.append(expense)


for i in range(num_expenses):
    print("Barang no ", i+1, ": ", expenses[i][0])
    print("Harga barang: ", expenses[i][1])

total = 0
for expense in expenses:
    total += expense[1]
    

print("Total:", total)