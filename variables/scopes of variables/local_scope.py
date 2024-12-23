"""
Scope of a Variables:
    There are two methods how we can define scope of a variables in python. They are:
    1. Local Variable
    2. Global Variable
"""
"""
1. Local Variable:
    Variables defined inside a function are local to that function.
"""
# For Example:

# function for greeting
def greeting():
    greet = "Hello"
    print(greet)

# calling function:
greeting()  
print(greet)  # This would raise an error since local_variable is not accessible outside the function.

