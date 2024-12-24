"""
Python Function Arguments:
    Arguments are the values passed inside the parenthesis of the function. 
    A function can have any number of arguments separated by a comma.

    Syntax:
        def functuion_name(parameter1. parameter2, ....):
            statement(s)
            return expression 
"""
# For Example:
def even_or_odd(num):
    if (num % 2 == 0):
        print(f"{num} is an even number")   # output: 40 is an even number
    else:
        print(f"{num} is an even number")

x = 40
# calling the even_or_odd() function
result = even_or_odd(x)
