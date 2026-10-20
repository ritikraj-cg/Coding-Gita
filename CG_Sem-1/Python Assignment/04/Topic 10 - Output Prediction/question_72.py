marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

# 95 -> A
# 85 -> B
# 50 -> Pass
# 30 -> Fail
#
# Conditions are checked from top to bottom.
# A more specific higher range must be checked before a broader lower range.
