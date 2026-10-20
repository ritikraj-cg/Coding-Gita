print("1. Pizza - ₹250")
print("2. Burger - ₹150")
print("3. Pasta - ₹200")
print("4. Sandwich - ₹120")

choice, quantity = input("Enter choice and quantity: ").split()
choice = int(choice)
quantity = int(quantity)

match choice:
    case 1:
        item = "Pizza"
        price = 250
    case 2:
        item = "Burger"
        price = 150
    case 3:
        item = "Pasta"
        price = 200
    case 4:
        item = "Sandwich"
        price = 120
    case _:
        print("Invalid Choice")
        price = 0
        item = ""

if price > 0:
    total = price * quantity

    if total >= 500:
        discount = total * 10 / 100
    else:
        discount = 0

    final_amount = total - discount

    print(f"Item: {item}")
    print(f"Total: {total}")
    print(f"Discount: {discount:.2f}")
    print(f"Final: {final_amount:.2f}")
