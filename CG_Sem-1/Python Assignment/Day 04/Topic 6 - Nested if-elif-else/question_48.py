stock, payment_status = input("Enter stock and payment status: ").split()

stock = int(stock)

if stock > 0:
    if payment_status == "paid":
        print("Order Confirmed")
    elif payment_status == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")
