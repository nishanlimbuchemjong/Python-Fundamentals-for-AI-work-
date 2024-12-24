"""
Arbitrary Keyword  Arguments:
    In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. 

    There are two special symbols:

    1. *args in Python (Non-Keyword Arguments):
        It allows a function to accept any number of positional (non-keyword) arguments.
        How it works:
            - The arguments are packed into a tuple inside the function.
            - We can loop through them or access them by index.
    2. **kwargs in Python (Keyword Arguments):L
        It allows a function to accept any number of keyword (named) arguments
        How it works:
            - The arguments are packed into a dictionary inside the function.
            - We can access them by their keys.
"""
# For Example: Variable length non-keywords argument
print("*args in Python Example:")
def say(*args):
    for arg in args:
        print(arg)

say('Hello', 'I', 'am', 'Nishan', 'Limbu')
"""
Output: 
Hello
I
am
Nishan
Limbu
"""

# For Example: Variable length keyword arguments
print("\n**kwargs in Python Example:\n")
def greeting(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greeting(first='Hello', mid='Nishan', last='Limbu')

"""
Output:
first: Hello
mid: Nishan
last: Limbu
"""