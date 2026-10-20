number = 4726

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

reversed_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands

print("Original Number:", number)
print("Reversed Number:", reversed_number)
