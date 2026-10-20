days = int(input("Enter number of days: "))
total = 0
above = 0
for i in range(days):
    units = int(input("Enter units: "))
    total = total + units
    if units > 10:
        above = above + 1
print("Total Units:", total)
print("Days Above 10:", above)
