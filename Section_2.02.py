# 🔰 Standard library import
import math  # standard library module

# 🧪 Third-party import (if applicable)
# import requests  # example of a third-party library

# 🧩 Local module import
# from mymodule.utils import helper_function  # example of a local import


# 🧮 Constants (ALL_CAPS naming convention)
MAX_RETRIES = 3
PI = 3.1416


# 🧾 Function with proper docstring and naming
def calculate_circle_area(radius):
    """
    Calculate the area of a circle given the radius.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: Area of the circle.
    """
    return PI * radius ** 2  # formula: π * r^2


# 🧪 Example of a block comment
# This function checks if a user is active
# and prints a personalized greeting.
def greet_user(user_name):
    """
    Greet the user by name if they are active.

    Parameters:
        user_name (str): The user's name.
    """
    # Use single or double quotes consistently
    greeting = f"Hello, {user_name}!"  # formatted string

    print(greeting)  # ✅ inline comment: brief and useful


# 🧠 Main logic with programming best practices
def main():
    """
    Main function to demonstrate all best practices.
    """
    # Avoid magic numbers — use named constants
    radius = 5  # example input

    # ✅ Correct use of whitespace and operators
    area = calculate_circle_area(radius)

    # ✅ Inline comment with 2 spaces before
    print(f"The area of the circle is: {area}")  # display area

    # Loop with exception handling — avoid global variables
    for attempt in range(MAX_RETRIES):
        try:
            # Simulate a user input or login
            user_name = "Disha"  # pretend input
            greet_user(user_name)
            break  # exit loop on success
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == MAX_RETRIES - 1:
                raise  # re-raise the last exception


# 👇 Standard way to call main in Python
if __name__ == '__main__':
    main()
