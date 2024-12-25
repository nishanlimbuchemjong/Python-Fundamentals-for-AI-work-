"""
Default Arguments:
    A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
"""
# For Example:
def sum(x, y=10):
    return x + y

a = 50
# calling the funciton:
result = sum(a)

# printing the sum of two numbers
print(f"Sum: {result}")  # output: Sum: 60