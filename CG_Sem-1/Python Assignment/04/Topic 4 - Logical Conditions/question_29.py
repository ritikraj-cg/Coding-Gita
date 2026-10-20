marks, attendance = input("Enter marks and attendance: ").split()

marks = float(marks)
attendance = float(attendance)

if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")
