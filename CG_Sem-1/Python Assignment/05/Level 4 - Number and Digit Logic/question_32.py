n = int(input("Enter a number: "))
target = int(input("Enter target digit: "))
temp = n
count = 0
for i in range(n):
    if temp > 0:
        if temp % 10 == target:
            count = count + 1
        temp = temp // 10
print(count)
