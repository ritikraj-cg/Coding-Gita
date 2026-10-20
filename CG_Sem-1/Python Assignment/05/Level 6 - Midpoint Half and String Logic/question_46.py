text = input("Enter an even-length string: ")
middle = len(text) // 2
first = ""
second = ""
index = 0
for ch in text:
    if index < middle:
        first = first + ch
    else:
        second = second + ch
    index = index + 1
print("First Half:", first)
print("Second Half:", second)
