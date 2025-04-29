def greet(greeting, *args, **kwargs):
    print(greeting)
    for name in args:
        print(f"Hello, {name}!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Passing positional arguments (names) and keyword arguments (info)
greet("Good Morning", "Alice", "Bob", age=25, city="London")
