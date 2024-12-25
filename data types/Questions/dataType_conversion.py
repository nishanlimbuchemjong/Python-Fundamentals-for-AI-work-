"""
Write a Python program that:

Defines two variables: num_str (a string) and num_int (an integer). 
Assign values like "10" to num_str and 5 to num_int.

Convert num_str to an integer and calculate its sum with num_int.
Print the result in the format:
"The sum of [num_str] and [num_int] is [result]."

"""

num_str = "10"
num_int = 5

# converting string to integer
convert_str_to_int = int(num_str)

# adding 
sum = num_int + convert_str_to_int
print(f"The sum of {num_str} and {num_int} is {sum}")

# Output: The sum of 10 and 5 is 15
