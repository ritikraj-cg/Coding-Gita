age, test_status = input("Enter age and test status: ").split()

age = int(age)

if age >= 18:
    if test_status == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")
