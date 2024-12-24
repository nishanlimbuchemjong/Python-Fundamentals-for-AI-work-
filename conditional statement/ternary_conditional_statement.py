"""
 Ternary Expression Conditional Statements in Python:
    The Python ternary Expression determines if a condition is true or false and then returns 
    the appropriate value in accordance with the result. 
    The ternary Expression is useful in cases where we need to assign a value to a variable based on a 
    simple condition, and we want to keep our code more concise — all in just one line of code.

    Syntax: 
        [on_true] if (expression) else [on_false]
"""
# For Example:
x, y = 20, 25

print(f"{x} is greater than {y}") if (x > y) else print(f"{x} is less than {y}")    # output: 20 is less than 25