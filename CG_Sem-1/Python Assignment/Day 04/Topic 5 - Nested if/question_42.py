year, attendance = input("Enter year and attendance: ").split()

year = int(year)
attendance = float(attendance)

if year == 2 or year == 3 or year == 4:
    if attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")
