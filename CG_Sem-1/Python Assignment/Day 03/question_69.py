student_code = input("Enter student code: ")
parts = student_code.split("-")
degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = parts[3]
roll_from_slice = student_code[-3:]
print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll_from_slice}")
print(f"Code: {degree}/{branch}/{roll_from_slice}")
