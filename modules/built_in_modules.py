"""
Use of different Built-in Modules in Python:
"""
# For Example:

# using math module:  Mathematical functions.
print("Using math module:")
import math

print(math.sqrt(5))   # output: 2.23606797749979

# using os module: Interact with the operating system.
print("Using os module:")
import os

print(os.getcwd())  # output: C:\Users\user\Desktop\AI Engineer Learning\Python Fundamentals\modules


# using sys module: Access system-specific parameters and functions.
print("Using sys module:")
import sys

print(sys.version)  # output: 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]

# using random module: Generate random numbers.
print("Using random module:")
import random as r

print(r.randint(1, 20))  # output: 17


# using datetime module:  Work with dates and times.
print("Using datetime module:")
from datetime import datetime

print(datetime.now())  # output: 2024-12-25 01:05:35.694930