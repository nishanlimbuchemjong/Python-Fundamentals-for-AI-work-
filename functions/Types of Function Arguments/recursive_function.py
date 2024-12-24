"""
Recursive Functions in Python:
    A recursive function is a function that calls itself to solve smaller instances of a problem until it reaches a base case (a condition to stop the recursion). 
    Recursive functions are useful for problems that can be broken down into smaller, similar sub-problems.
"""
# Example  1:
print("Example of Factorial:")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
# calling the function:
result = factorial(num)

print(f"Factorial of {num} is {result}")    # output: Factorial of 5 is 120

# Example  2:
print("\nExample of Fibonacci Sequence:")
def fibonacci_sequence(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

num = 6
# calling the function:
result = fibonacci_sequence(num)
print(f"Fibonacci sequence of {num} is {result}")    # output: Fibonacci sequence of 6 is 8

# Example  3:
print("\nExample of Sum of Digits:")
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)

num = 345
# calling the function:
result = sum_of_digits(num)
print(f"Sum of digit of a number '{num}' is {result}")    # output: Sum of digit of a number '345' is 12
