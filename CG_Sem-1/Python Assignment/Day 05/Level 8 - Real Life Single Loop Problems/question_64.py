days = int(input("Enter working days: "))
present = 0
absent = 0
for i in range(days):
    status = input("Enter P or A: ").upper()
    if status == "P":
        present = present + 1
    else:
        absent = absent + 1
percentage = present / days * 100
print("Present:", present)
print("Absent:", absent)
print("Attendance:", round(percentage, 2), "%")
