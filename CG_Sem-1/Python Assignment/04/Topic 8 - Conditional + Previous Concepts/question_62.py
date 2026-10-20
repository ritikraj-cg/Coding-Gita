price, quantity = input("Enter price and quantity: ").split()

price = float(price)
quantity = int(quantity)

subtotal = price * quantity

if subtotal >= 5000:
    discount_percentage = 20
elif subtotal >= 2000:
    discount_percentage = 10
else:
    discount_percentage = 0

discount = subtotal * discount_percentage / 100
final_amount = subtotal - discount

print(f"Subtotal: {subtotal:.0f}")
print(f"Discount: {discount_percentage}%")
print(f"Final: {final_amount:.2f}")
