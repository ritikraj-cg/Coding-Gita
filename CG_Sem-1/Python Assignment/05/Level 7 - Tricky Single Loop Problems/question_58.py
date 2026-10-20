n = int(input("Enter a positive number: "))
temp = n
total = 0
sign = 1
for i in range(n):
    if temp > 0:
        digit = temp % 10
        total = total + digit * sign
        sign = sign * -1
        temp = temp // 10
print(total)
