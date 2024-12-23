"""
Set Data Type:
    It is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. 
    The order of elements in a set is undefined though it may consist of various elements.

    Sets can be created by using the built-in set() function with an iterable object or a sequence 
    by placing the sequence inside curly braces, separated by a ‘comma’. 
    The type of elements in a set need not be the same, various mixed-up data type values can also be passed 
    to the set.
"""
# For Example:

s1 = set()
s1 = set("Nishan Limbu")
print("Welcome, ", s1)  # output: Welcome, {'a', 'u', 'm', 's', 'b', ' ', 'N', 'i', 'L', 'h', 'n'}

s2 = set(["ML", "AI", "DSA"])
print(s2)       # output: {'AI', 'DSA', 'ML'}

# Accessing Set items:
"""
Set items cannot be accessed by referring to an index, since sets are unordered the items have no index. 
But we can loop through the set items using a for loop, or ask if a specified value is present in a set, 
by using the 'in' the keyword.
"""
# For Example:
set1 = set(["ML", "AI", "DSA"])

# looping through set1:
for i in set1:
    print(i, end=" ")   # output: AI DSA ML

# checking if item exists in set1
print("ML" in set1)     # output: True