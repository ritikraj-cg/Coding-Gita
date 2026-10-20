n = int(input("Enter a positive number: "))
temp = n
even = 0
odd = 0
for i in range(n):
    if temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        temp = temp // 10
if even > odd:
    print("More Even Digits")
elif odd > even:
    print("More Odd Digits")
else:
    print("Equal")
