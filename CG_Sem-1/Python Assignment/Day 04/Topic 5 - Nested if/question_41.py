amount, payment_method = input("Enter order amount and payment method: ").split()

amount = float(amount)

if amount >= 500:
    if payment_method == "card":
        print("Card Payment Accepted")
    elif payment_method == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")
