student_id = input("Enter student ID: ")
degree, batch, branch, roll_number = student_id.split("-")
last_three = student_id[-3:]
roll_number = int(roll_number)
print("Degree:", degree)
print("Batch:", batch)
print("Branch:", branch)
print("Roll Number:", roll_number)
print("Last Three Characters:", last_three)
