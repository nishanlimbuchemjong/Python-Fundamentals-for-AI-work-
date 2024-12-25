"""
Python Function with Parameters:
    Syntax:
        def function_name(parameter: data_type) -> return_type:
            statement(s)
            return expression
 
"""
# For Example:

def sum(x: int, y: int) -> int:
    return x + y

a, b = 10, 20
# calling the funciton:
result = sum(a, b)

# printing the result:
print(f"Sum of {a} and {b} is {result}")    # output: Sum of 10 and 20 is 30