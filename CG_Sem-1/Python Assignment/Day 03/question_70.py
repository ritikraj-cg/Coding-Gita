full_name = input("Enter full name: ")
words = full_name.split()
first_name = words[0]
last_name = words[-1]
first_name_upper_part = first_name[:3].upper()
last_name_lower_part = last_name[2:5].lower()
reversed_name = full_name[::-1]
print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_name_upper_part}")
print(f"Last Name (Lower Part): {last_name_lower_part}")
print(f"Full Name Reversed: {reversed_name}")
