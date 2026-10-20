n = int(input("Enter a positive number: "))
temp = n
digits = 0
for i in range(n):
    if temp > 0:
        digits = digits + 1
        temp = temp // 10
print(digits)
