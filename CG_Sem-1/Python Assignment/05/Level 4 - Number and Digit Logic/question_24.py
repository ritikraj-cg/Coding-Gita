n = int(input("Enter a number: "))
temp = n
total = 0
for i in range(n):
    if temp > 0:
        total = total + temp % 10
        temp = temp // 10
print(total)
