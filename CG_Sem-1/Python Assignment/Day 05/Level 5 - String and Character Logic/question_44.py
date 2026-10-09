text = input("Enter a string: ")
result = ""
for ch in text:
    if ch.lower() not in "aeiou":
        result = result + ch
print(result)
