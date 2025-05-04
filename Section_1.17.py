import functools

# 1. Basic decorator with logging and metadata preservation
def log_decorator(func):
    @functools.wraps(func)  # Preserves the function's name, docstring
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] '{func.__name__}' returned: {result}")
        return result
    return wrapper

# 2. Decorator with arguments to repeat the function call
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                print(f"Repeat {i+1} of {n}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# 3. Final decorated function using both decorators
@repeat(3)              # Outer decorator: repeats 3 times
@log_decorator          # Inner decorator: logs the function
def greet(name):
    """Greets the user with their name."""
    print(f"Hello, {name}!")
    return f"Greeting sent to {name}"

# Run the decorated function
greet("Alice")

# Check preserved metadata
print("\nFunction name:", greet.__name__)
print("Docstring:", greet.__doc__)
