text = input("Enter a string: ")
vowels = 0
consonants = 0
for ch in text:
    if ch != " ":
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
print("Vowels =", vowels, "Consonants =", consonants)
