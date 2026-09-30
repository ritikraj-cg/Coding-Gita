age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")

# age = 20, has_id = False -> ID Required
# age = 16, has_id = True -> Underage
