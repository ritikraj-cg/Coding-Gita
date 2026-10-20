n = int(input("Enter a number: "))
temp = n
product = 1
for i in range(n):
    if temp > 0:
        product = product * (temp % 10)
        temp = temp // 10
print(product)
