price = 2000
discount = 15
gst = 18

discount_amount = price * discount / 100
price_after_discount = price - discount_amount
gst_amount = price_after_discount * gst / 100
final_price = price_after_discount + gst_amount

print("Discount Amount:", discount_amount)
print("Price After Discount:", price_after_discount)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)
