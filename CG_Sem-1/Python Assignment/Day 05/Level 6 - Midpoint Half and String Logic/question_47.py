text = input("Enter a string: ")
count = len(text)
first = ""
middle = ""
second = ""
index = 0
for ch in text:
    if count % 2 == 1 and index == count // 2:
        middle = ch
    elif index < count // 2:
        first = first + ch
    else:
        second = second + ch
    index = index + 1
print("First Half:", first)
if count % 2 == 1:
    print("Middle:", middle)
print("Second Half:", second)
