message = "a"

def greet(name):
     message = "b"

#   def send_email(name):
#        message = "b" we can modify it by "global message" but its bad bc can affect side stuff

greet("Emil")
print(message)