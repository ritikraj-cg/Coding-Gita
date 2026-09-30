marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

# The original program checked marks >= 40 first.
# Therefore 80 and 95 were caught by "Pass" before reaching A or B.
