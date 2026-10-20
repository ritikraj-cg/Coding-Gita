number = 5829

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

print("Ones Digit:", ones)
print("Tens Digit:", tens)
print("Hundreds Digit:", hundreds)
print("Thousands Digit:", thousands)
