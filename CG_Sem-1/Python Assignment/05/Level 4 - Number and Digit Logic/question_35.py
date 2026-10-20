n = int(input("Enter a positive number: "))
temp = n
position = 1
for i in range(n):
    if temp > 0:
        print(temp % 10, position)
        temp = temp // 10
        position = position + 1
