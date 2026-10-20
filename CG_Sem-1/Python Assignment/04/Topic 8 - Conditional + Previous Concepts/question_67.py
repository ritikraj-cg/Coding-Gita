distance, ride_type = input("Enter distance and ride type: ").split()

distance = float(distance)

match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        print("Invalid Ride Type")
        rate = 0

if rate > 0:
    fare = distance * rate

    if distance > 20:
        fare = fare + fare * 10 / 100

    print(f"Fare: {fare:.2f}")
