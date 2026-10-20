text = input("Enter a string: ")
same = True
for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        same = False
if same:
    print("Symmetric")
else:
    print("Not Symmetric")
