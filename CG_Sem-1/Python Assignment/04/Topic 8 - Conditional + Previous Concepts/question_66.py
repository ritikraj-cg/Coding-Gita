marks1, marks2, marks3, attendance = input("Enter three marks and attendance: ").split()

marks1 = float(marks1)
marks2 = float(marks2)
marks3 = float(marks3)
attendance = float(attendance)

total = marks1 + marks2 + marks3
average = total / 3

if attendance >= 75:
    if average >= 90:
        print("Outstanding")
    elif average >= 75:
        print("Very Good")
    elif average >= 60:
        print("Good")
    elif average >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")
