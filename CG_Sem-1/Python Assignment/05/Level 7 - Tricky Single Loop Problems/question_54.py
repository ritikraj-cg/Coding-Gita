text = input("Enter a string: ")
current = 0
best = 0
previous = ""
for ch in text:
    if ch == previous:
        current = current + 1
    else:
        current = 1
    if current > best:
        best = current
    previous = ch
print(best)
