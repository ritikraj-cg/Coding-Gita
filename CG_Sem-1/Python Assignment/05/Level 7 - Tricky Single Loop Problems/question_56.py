n = int(input("Enter a positive number: "))
temp = n
total = 0
for i in range(n):
    if temp > 0:
        total = total + temp % 10
        print(total)
        temp = temp // 10
