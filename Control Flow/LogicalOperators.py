# 3 logical operators
# and
# or
# not
high_income = True
good_credit = True
student = False
if (high_income or good_credit) and not student:
 #if not student:
 #if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")