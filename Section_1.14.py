def outer_function(outer_var):
    # Outer function with an argument `outer_var`
    def inner_function(inner_var):
        # Inner function that uses `outer_var` from the outer function's scope
        return outer_var + inner_var
    return inner_function

# Creating a closure
closure_example = outer_function(5)

# Calling the closure
result = closure_example(10)
print(result)  # Output: 15
