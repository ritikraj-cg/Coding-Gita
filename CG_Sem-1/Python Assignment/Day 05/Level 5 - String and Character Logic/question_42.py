text = input("Enter a string: ")
upper = 0
lower = 0
for ch in text:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
print("Uppercase =", upper, "Lowercase =", lower)
