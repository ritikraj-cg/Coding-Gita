text = input("Enter an even-length string: ")
half = len(text) // 2
same = True
for i in range(half):
    if text[i] != text[i + half]:
        same = False
if same:
    print("Equal Halves")
else:
    print("Different Halves")
