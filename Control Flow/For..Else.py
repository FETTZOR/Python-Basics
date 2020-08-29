successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Succesful!")
        break
else:
    print("Attempted 3 times and failed")