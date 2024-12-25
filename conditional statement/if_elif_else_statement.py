"""
If-elif-else Conditional Statements in Python:
    The if statements are executed from the top down. As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. 
    If none of the conditions is true, then the final “else” statement will be executed.

    Syntax:
        if condition:
            statement(s)
        elif condition:
            statement(s)
        elfi condition:
            statement(s)
        .
        .
        .
        else:
            statement(s)
"""
# For Example:

x = 10

if (x < 10):
    print(f"{x} is less than 10.")
elif (x > 10):
    print(f"{x} is greater than 10.")
else:
    print(f"{x} is equal to 10.")   # output: 10 is equal to 10.
