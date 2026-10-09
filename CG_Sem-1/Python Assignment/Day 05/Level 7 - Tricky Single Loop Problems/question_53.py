n = int(input("Enter a number: "))
temp = n
largest = -1
second = -1
for i in range(n):
    if temp > 0:
        digit = temp % 10
        if digit > largest:
            second = largest
            largest = digit
        elif digit < largest and digit > second:
            second = digit
        temp = temp // 10
print(second)
