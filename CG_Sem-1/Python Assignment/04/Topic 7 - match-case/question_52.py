a, b, operator = input("Enter two numbers and operator: ").split()

a = float(a)
b = float(b)

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid Operator")
