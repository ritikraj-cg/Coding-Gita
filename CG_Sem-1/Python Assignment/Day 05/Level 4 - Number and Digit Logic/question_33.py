n = int(input("Enter a positive number: "))
temp = n
for i in range(n):
    if temp >= 10:
        temp = temp // 10
print(temp)
