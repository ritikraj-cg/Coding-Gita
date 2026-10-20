text = input("Enter an odd-length string: ")
count = 0
for ch in text:
    count = count + 1
print(text[count // 2])
