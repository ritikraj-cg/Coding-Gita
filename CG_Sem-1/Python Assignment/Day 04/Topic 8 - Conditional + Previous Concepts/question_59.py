email = input("Enter email: ")

username, domain = email.split("@")

if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")
