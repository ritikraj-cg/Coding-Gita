age, distance = input("Enter age and distance: ").split()

age = int(age)
distance = float(distance)

if age < 5:
    print("Free")
elif age >= 60:
    print("Senior")
else:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")
