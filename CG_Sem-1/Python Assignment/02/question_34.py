number = 9365

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)
