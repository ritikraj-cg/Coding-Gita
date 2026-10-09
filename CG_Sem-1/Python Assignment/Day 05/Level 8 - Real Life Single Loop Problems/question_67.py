n = int(input("Enter number of attempts: "))
success = 0
failed = 0
for i in range(n):
    result = input("Enter success or failed: ").lower()
    if result == "success":
        success = success + 1
    else:
        failed = failed + 1
rate = success / n * 100
print("Successful:", success)
print("Failed:", failed)
print("Success Rate:", rate, "%")
