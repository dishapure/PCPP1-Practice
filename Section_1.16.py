# Class-based decorator
class UpperCaseDecorator:
    def __init__(self, func):
        self.func = func  # Store the original function

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)  # Call the original function
        return result.upper()  # Modify and return the result

@UpperCaseDecorator
def greet():
    return "hello from the function"

# Calling the decorated function
print(greet())  # Output: HELLO FROM THE FUNCTION
