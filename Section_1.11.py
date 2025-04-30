def greet_user(name):
    print(f"Hello, {name}!")

def say_hello(name):
    greet_user(name)  # Forwarding the argument to greet_user

# Test it
say_hello("Disha")
say_hello("Ravi")
