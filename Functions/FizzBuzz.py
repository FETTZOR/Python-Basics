# if input divisible by 3 return Fizz
# if input divisible by 5 return Buzz
# if input divisible by 3 and 5 (both) return FizzBuzz
# if not divisible by 3 or 5 return input
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
       return "FizzBuzz"
    if input % 3 == 0:
       return"Fizz"
    if input % 5 == 0:
       return"Buzz"
    elif input % 3 != 0 and input % 5 != 0:
       return input

print(fizz_buzz(7))

