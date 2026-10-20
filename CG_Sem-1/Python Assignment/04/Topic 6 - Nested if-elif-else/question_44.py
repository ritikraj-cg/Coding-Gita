a, b, c = input("Enter three integers: ").split()

a = int(a)
b = int(b)
c = int(c)

if a == b and b == c:
    print("All are Equal")
elif a == b and a > c:
    print("A and B are Equal and Greatest")
elif a == c and a > b:
    print("A and C are Equal and Greatest")
elif b == c and b > a:
    print("B and C are Equal and Greatest")
elif a > b:
    if a > c:
        print("A is Greatest")
    else:
        print("C is Greatest")
else:
    if b > c:
        print("B is Greatest")
    else:
        print("C is Greatest")
