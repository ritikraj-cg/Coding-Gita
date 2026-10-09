text = input("Enter a string: ")
target = input("Enter target character: ")
count = 0
for ch in text:
    if ch == target:
        count = count + 1
print(count)
