"""
Variables act as a placeholder for data. They allow use to store and reuse values in our program.

"""
# For Example:

x = 10 # variable 'x' stores the integer value 10

name = 'Nishan Limbu' # variable 'name' stores the string 'Nishan Limbu'

"""
Rules for Naming Variables:
    1. Variable names can only contain letters, digits and underscores (_).
    2. A variable name cannot start with a digit.
    3. Variable names are case-sensitive (myProject and myproject are different).
    4. Avoid using Python keywords (e.g., if, else, for) as variable names.
"""
# For Example:

# Valid Example:
age = 25
_color = 'black'
total_score = 350

# Invalid Example:
# 1name = "Nishan"     # Starts with a digits
# class = 10     # 'class' is a reserved keyword
# user-name = 'nishan'    #contains a hyphen

"""
Assigning Different Values:
    we can assign different values to multiple variables simultaneously, 
    making the code concise and easier to read.
"""
# For Example:
x, y, z = 1, 2.4, "Nishan"
print(x, y, z)      #output:  1       2.4        Nishan

"""
Casting a Variable:
    Casting refers to the process of converting the value of one data type into another.
    Python provides several built-in functions to facilitate casting, including int(), 
    float() and str() among others.

    i. int(): converts compatible values to an integer.
    ii. float(): transforms values into floating-point numbers.
    iii. str(): converts any data type into a string.
"""
# For Example:
x = "10"
number = int(x)   # converts str to integer
print(f"integer number: {number}")       

float_number = float(number)  # converts integer to float
print(f"floating number: {float_number}")

age = 25
str_age = str(age)    #converts integer to string
print(f"age: {str_age}")
