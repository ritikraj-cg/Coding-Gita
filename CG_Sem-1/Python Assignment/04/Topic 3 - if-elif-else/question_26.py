a, b, operator = input("Enter two numbers and operator: ").split()

a = float(a)
b = float(b)

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid Operator")
