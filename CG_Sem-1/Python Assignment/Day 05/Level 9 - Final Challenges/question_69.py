text = input("Enter a string: ")
total = 0
vowels = 0
consonants = 0
upper = 0
lower = 0
even_index = 0
index = 0
for ch in text:
    total = total + 1
    if index % 2 == 0:
        even_index = even_index + 1
    if ch != " ":
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        elif ch.isalpha():
            consonants = consonants + 1
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
    index = index + 1
print("Total Characters:", total)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Even Index Characters:", even_index)
