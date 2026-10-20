age, ticket_type = input("Enter age and ticket type: ").split()

age = int(age)

if age < 5:
    print("Free Travel")
elif age >= 60:
    print("Senior Passenger")
else:
    if ticket_type == "AC":
        print("AC Ticket")
    elif ticket_type == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")
