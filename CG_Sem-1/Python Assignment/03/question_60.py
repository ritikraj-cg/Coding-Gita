name = input("Enter student name: ")
marks1, marks2, marks3 = input("Enter three marks: ").split()
marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)
total = marks1 + marks2 + marks3
average = total / 3
print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
