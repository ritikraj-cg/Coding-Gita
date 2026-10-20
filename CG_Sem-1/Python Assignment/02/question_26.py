number = 583

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

sum_of_digits = ones + tens + hundreds

print("Sum of Digits:", sum_of_digits)
