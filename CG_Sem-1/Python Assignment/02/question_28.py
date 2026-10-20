number = 234

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

product_of_digits = ones * tens * hundreds

print("Product of Digits:", product_of_digits)
