text = input("Enter a string: ")
even = 0
odd = 0
for i in range(len(text)):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even Index =", even, "Odd Index =", odd)
