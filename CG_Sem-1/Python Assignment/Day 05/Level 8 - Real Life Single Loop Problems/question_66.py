products = int(input("Enter number of products: "))
total = 0
above = 0
for i in range(products):
    price = int(input("Enter price: "))
    total = total + price
    if price > 1000:
        above = above + 1
print("Total Bill:", total)
print("Products Above 1000:", above)
