student_id = input("Enter student ID: ")

degree, batch, branch, roll_number = student_id.split("-")

if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")
