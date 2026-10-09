text = input("Enter a string: ")
target = input("Enter target character: ")
position = -1
index = 0
for ch in text:
    if ch == target and position == -1:
        position = index
    index = index + 1
if position == -1:
    print("Not Found")
else:
    print(position)
