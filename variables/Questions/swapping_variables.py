"""
Write a Python program that:

Defines two variables, x and y, with values of your choice.
Swaps the values of these two variables without using a third variable.
Prints the values of x and y before and after swapping.

"""
x = 20
y = 40

print(f"Before swapping: x = {x}, and y = {y}")

# swapping values of x and y without using third variables
x = x + y
y = x - y
x = x - y
print(f"After swapping: x = {x}, and y = {y}")
