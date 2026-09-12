number = 5836

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

sum_of_digits = ones + tens + hundreds + thousands
reversed_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands

print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)
print("Sum of Digits:", sum_of_digits)
print("Reversed Number:", reversed_number)

price = "1250"
quantity = "4"
discount = "10"

price = int(price)
quantity = int(quantity)
discount = int(discount)

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)
