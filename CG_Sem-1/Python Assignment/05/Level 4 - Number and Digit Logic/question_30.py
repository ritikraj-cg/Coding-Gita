n = int(input("Enter a positive number: "))
temp = n
reverse = 0
for i in range(n):
    if temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
print(reverse)
