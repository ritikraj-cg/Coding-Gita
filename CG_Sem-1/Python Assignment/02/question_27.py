number = 4726

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

sum_of_digits = ones + tens + hundreds + thousands

print("Sum of Digits:", sum_of_digits)
