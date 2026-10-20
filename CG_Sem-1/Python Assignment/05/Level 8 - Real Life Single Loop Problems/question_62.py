days = int(input("Enter number of days: "))
total = 0
highest = 0
lowest = 0
for i in range(days):
    expense = int(input("Enter expense: "))
    total = total + expense
    if i == 0:
        highest = expense
        lowest = expense
    else:
        if expense > highest:
            highest = expense
        if expense < lowest:
            lowest = expense
print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)
