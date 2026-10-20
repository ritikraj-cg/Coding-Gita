text = input("Enter a string: ")
target = input("Enter target character: ")
count = 0
length = 0
for ch in text:
    length = length + 1
    if ch == target:
        count = count + 1
if length > 0:
    frequency = count / length * 100
else:
    frequency = 0
print("Count =", count, "Frequency =", round(frequency, 2), "%")
