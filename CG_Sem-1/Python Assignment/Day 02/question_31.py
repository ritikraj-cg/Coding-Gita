number = 5834

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

print("Thousands Place:", thousands * 1000)
print("Hundreds Place:", hundreds * 100)
print("Tens Place:", tens * 10)
print("Ones Place:", ones)
