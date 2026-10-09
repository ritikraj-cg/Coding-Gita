n = int(input("Enter a number: "))
temp = n
total = 0
for i in range(n):
    if temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            total = total + digit
        temp = temp // 10
print(total)
