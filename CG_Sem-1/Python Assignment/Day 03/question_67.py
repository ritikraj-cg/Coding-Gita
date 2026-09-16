date = input("Enter date: ")
day, month, year = date.split("-")
year_from_slice = date[-4:]
print("Day:", day)
print("Month:", month)
print("Year:", year)
print("Year using slicing:", year_from_slice)
