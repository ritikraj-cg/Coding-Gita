a, b = input("Enter two integers: ").split()

a = int(a)
b = int(b)

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Both are Equal")
