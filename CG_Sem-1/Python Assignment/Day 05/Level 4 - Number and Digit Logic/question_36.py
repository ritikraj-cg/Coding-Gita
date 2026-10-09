n = int(input("Enter a 3-digit number: "))
temp = n
total = 0
for i in range(3):
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10
if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
