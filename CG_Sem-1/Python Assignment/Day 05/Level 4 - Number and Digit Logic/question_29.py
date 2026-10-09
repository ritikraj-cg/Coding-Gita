n = int(input("Enter a number: "))
temp = n
smallest = 9
for i in range(n):
    if temp > 0:
        digit = temp % 10
        if digit < smallest:
            smallest = digit
        temp = temp // 10
print(smallest)
