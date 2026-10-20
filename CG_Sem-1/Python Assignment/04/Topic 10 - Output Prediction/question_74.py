choice = 5

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")

# 1 -> Add
# 3 -> Delete
# 5 -> Invalid Choice
#
# case _ is the default case for values that do not match another case.
