full_name = input("Enter full name: ")
words = full_name.split()
first_name = words[0]
last_name = words[2]
username = first_name.lower() + "." + last_name.lower()
print(username)
