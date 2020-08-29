age = 22
if age >= 18:
    message = "Eligible"
# print("Eligible")
else:
    message = "Not eligible"
# print("Not eligible")
message = "Eligible" if age >= 18 else "Not eligible" # same but shorter
print(message)