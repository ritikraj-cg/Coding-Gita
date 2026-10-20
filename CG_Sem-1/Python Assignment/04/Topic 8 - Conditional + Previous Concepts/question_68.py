score, percentage, category = input("Enter score, percentage and category: ").split()

score = float(score)
percentage = float(percentage)

match category:
    case "general":
        if score >= 80 and percentage >= 75:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case "obc":
        if score >= 70 and percentage >= 70:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case "sc":
        if score >= 60 and percentage >= 60:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case _:
        print("Admission Not Eligible")
