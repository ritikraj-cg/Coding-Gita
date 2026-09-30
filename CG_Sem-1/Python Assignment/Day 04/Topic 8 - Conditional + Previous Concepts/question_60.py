full_name = input("Enter full name: ")

first_name, middle_name, last_name = full_name.split()
username = first_name + "." + last_name

if "." in username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")
