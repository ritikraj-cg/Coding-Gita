marks, income = input("Enter marks and family income: ").split()

marks = float(marks)
income = float(income)

if marks >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")
