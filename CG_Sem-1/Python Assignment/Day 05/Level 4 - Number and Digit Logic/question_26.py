n = int(input("Enter a number: "))
temp = n
count = 0
for i in range(n):
    if temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            count = count + 1
        temp = temp // 10
print(count)
