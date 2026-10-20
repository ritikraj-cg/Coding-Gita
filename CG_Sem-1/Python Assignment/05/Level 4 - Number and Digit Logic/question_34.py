n = int(input("Enter a number: "))
temp = n
largest = 0
smallest = 9
for i in range(n):
    if temp > 0:
        digit = temp % 10
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        temp = temp // 10
print(largest - smallest)
