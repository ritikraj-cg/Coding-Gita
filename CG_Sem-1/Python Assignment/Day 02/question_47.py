price = "1500"
quantity = "2"
tax_rate = "5"

price = float(price)
quantity = int(quantity)
tax_rate = float(tax_rate)

subtotal = price * quantity
tax_amount = subtotal * tax_rate / 100
final_bill = subtotal + tax_amount

print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)
