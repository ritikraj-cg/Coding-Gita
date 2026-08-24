# ==================================================================
# A. BASIC UNDERSTANDING
# ==================================================================

# Q1: What is a variable?
# Answer:
# A variable is a named storage location in memory used to hold data/values
# that can be accessed and modified during program execution.


# Q2: Why are variables useful in programming?
# Answer:
# Variables make code reusable, dynamic, and easy to read. They allow us to
# store, update, and manipulate data repeatedly without hardcoding values.


# Q3: What is assignment?
# Answer:
# Assignment is the process of storing a value inside a variable using
# the assignment operator (=).


# Q4: What does the following statement do?
# age = 18
# Answer:
# It creates a variable named 'age' and assigns the integer value 18 to it.


# Q5: Explain the difference between a variable and its value.
# Answer:
# A variable is the identifier/name (container label), whereas the value is 
# the actual data stored inside that variable (e.g., in 'age = 18', 'age' is 
# the variable and '18' is its value).


# Q6: What is reassignment?
# Answer:
# Reassignment is changing the existing value of a variable by assigning a new 
# value to it later in the code.


# Q7: What happens to the current value of a variable when a new value is assigned to it?
# Answer:
# The old value is overwritten and replaced by the new value (the variable now points 
# to the new object in memory).


# Q8: What does it mean that Python variable names are case-sensitive?
# Answer:
# It means uppercase and lowercase letters are treated as completely different variables.
# For example, 'age', 'Age', and 'AGE' are three separate variables in Python.


# Q9: What is a naming convention?
# Answer:
# A naming convention is a set of rules and best practices for naming variables 
# to improve code readability and consistency among developers.


# Q10: What is `snake_case`?
# Answer:
# snake_case is a writing convention where words are written in lower case and 
# separated by underscores (_) (e.g., student_name, total_marks).


# ============================
# B. VARIABLE NAMING PRACTICE
# ============================

# Q11: Which of the following are valid variable names?

# name - Valid (starts with letters, no special characters)
# student_name - Valid (uses underscore, lowercase letters)
# 1student - Invalid (starts with a digit)
# student1 - Valid (contains letters and digits, starts with a letter)
# student name - Invalid (contains spaces)
# _total - Valid (starts with an underscore)


# Q12: Correct the invalid variable names:
# 1name         - name_1 or student_name
# student name  - student_name
# college-name  - college_name
# 2student_age  - student_age_2 or age_student_2


# Q13: Why is `student_name` generally better than `studentname` for readability?
# Answer:
# The underscore clearly separates distinct words, making it much easier to scan 
# and read quickly.


# Q14: Why is `student_name` generally better than `x` when storing a student's name?
# Answer:
# `student_name` is self-descriptive and meaningful, making the code self-documenting 
# and easier to understand, unlike 'x' which is generic.


# Q15: Are these names different in Python? (age, Age, AGE)
# Answer:
# Yes, because Python variable names are case-sensitive. All three refer to 
# different variables.


# Q16: Identify the naming convention used in: total_marks, student_name, phone_number
# Answer:
# snake_case (PEP 8 standard for Python variables).


# Q17: Write suitable variable names using Python's common naming convention:
student_name = "Rahul"
student_age = 18
student_city = "Patna"
total_marks = 450
college_name = "IIT Delhi"


# ==================================================================
# C. CODE UNDERSTANDING
# ==================================================================

# Q18: What values will the following variables refer to?
name = "Rahul"
age = 18
city = "Patna"
# Answer:
# name → "Rahul"
# age → 18
# city → "Patna"


# Q19: What is the final value of `age`?
age = 18
age = 19
# Answer:
# Final value of age is 19. The value 18 was overwritten by 19 during reassignment.


# Q20: What is the final value of `name`?
name = "Rahul"
name = "Amit"
name = "Riya"
# Answer:
# Final value of name is "Riya".


# Q21: Explain what happens in this program:
student_name = "Rahul"
student_age = 18
student_age = 19
# Explanation:
# 1. 'student_name' is assigned string "Rahul".
# 2. 'student_age' is initialized with integer 18.
# 3. 'student_age' is updated (reassigned) to 19, overwriting 18.


# Q22: What values will `a`, `b`, and `c` refer to?
a, b, c = 10, 20, 30
# Answer:
# a → 10
# b → 20
# c → 30


# Q23: What values will `x`, `y`, and `z` refer to?
x = y = z = 100
# Answer:
# x → 100
# y → 100
# z → 100


# ==================================================================
# D. PRACTICAL PROBLEMS
# ==================================================================

# Q24: Create variables for: Your name, Your age, Your city
my_name = "Aman"
my_age = 20
my_city = "Delhi"


# Q25: Create variables for: Student name, Student roll number, Student branch
student_name = "Priya"
student_roll_number = 101
student_branch = "Computer Science"


# Q26: Assign, reassign, and explain 'marks'
marks = 85  # Value before reassignment: 85
print("Before reassignment:", marks)

marks = 92  # Value after reassignment: 92
print("After reassignment:", marks)
# Explanation: 'marks' originally pointed to 85, but was updated to 92.


# Q27: Multiple assignment in one statement
name, age, city = "Rahul", 18, "Patna"


# Q28: Assign value 0 to three variables in one statement
x = y = z = 0


# Q29: Rewrite invalid variable names with valid ones
# Original (Invalid):
# 1student = "Rahul"
# student name = "Rahul"
# class = "B.Tech"

# Fixed (Valid):
student_1 = "Rahul"
student_name = "Rahul"
branch_class = "B.Tech"  # 'class' is a reserved keyword in Python


# Q30: Complete small Python program with comments, snake_case, and reassignment
# Program to manage student details and update age

student_name = "Ankit"
student_age = 18

print("Initial Details:")
print("Name:", student_name)
print("Age:", student_age)

# Reassigning new age after birthday
student_age = 19

print("\nUpdated Details:")
print("Name:", student_name)
print("Updated Age:", student_age)