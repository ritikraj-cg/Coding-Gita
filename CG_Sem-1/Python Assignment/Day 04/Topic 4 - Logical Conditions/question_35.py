amount, otp = input("Enter amount and OTP: ").split()

amount = float(amount)

if amount <= 50000 and otp == "1234":
    print("Transaction Approved")
else:
    print("Transaction Declined")
