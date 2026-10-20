balance, withdrawal = input("Enter balance and withdrawal amount: ").split()

balance = float(balance)
withdrawal = float(withdrawal)

if withdrawal <= balance:
    if withdrawal % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")
