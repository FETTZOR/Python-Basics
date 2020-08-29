 # def greet(name):
 #   #print(f"Hi {name}")
# return "..."
#print(greet("Emil"))


# 1 - Perform a task
# 2 - Return a value

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Emil")
file = open("context.txt", "w")
file.write(message)