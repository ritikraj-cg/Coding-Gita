n = int(input("Enter a number: "))
temp = n
largest = 0
for i in range(n):
    if temp > 0:
        digit = temp % 10
        if digit > largest:
            largest = digit
        temp = temp // 10
print(largest)
