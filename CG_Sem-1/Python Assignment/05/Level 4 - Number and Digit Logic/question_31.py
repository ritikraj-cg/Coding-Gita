n = int(input("Enter a number: "))
temp = n
reverse = 0
for i in range(n):
    if temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
if reverse == n:
    print("Palindrome")
else:
    print("Not Palindrome")
