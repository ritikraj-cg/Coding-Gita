n = int(input("Enter a positive number: "))
temp = n
digits = 0
total = 0
largest = 0
smallest = 9
even = 0
odd = 0
for i in range(n):
    if temp > 0:
        digit = temp % 10
        digits = digits + 1
        total = total + digit
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        if digit % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        temp = temp // 10
print("Digits:", digits)
print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Digits:", even)
print("Odd Digits:", odd)
