attendance, marks = input("Enter attendance and marks: ").split()

attendance = float(attendance)
marks = float(marks)

if attendance >= 75:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")
