text = input("Enter an even-length string: ")
result = ""
for i in range(0, len(text), 2):
    result = result + text[i + 1] + text[i]
print(result)
