number = 583

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

reversed_number = ones * 100 + tens * 10 + hundreds

print("Original Number:", number)
print("Reversed Number:", reversed_number)
