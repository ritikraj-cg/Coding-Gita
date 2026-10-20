subjects = int(input("Enter number of subjects: "))
total = 0
highest = 0
lowest = 0
for i in range(subjects):
    marks = int(input("Enter marks: "))
    total = total + marks
    if i == 0:
        highest = marks
        lowest = marks
    else:
        if marks > highest:
            highest = marks
        if marks < lowest:
            lowest = marks
average = total / subjects
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
