"""
List Comprehension in Python:
    List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

    Syntax:
        [expression for item in iterable if condition]

        where,
            expression: The transformation or value to be included in the new list.
            item: The current element taken from the iterable.
            iterable: A sequence or collection (e.g., list, tuple, set).
            if condition (optional): A filtering condition that decides whether the current item should be included.

"""
# For example:
    # if we have a list of integers and want to create a new list containing the square of each element, 
    # we can easily achieve this using list comprehension.

x = [1, 2, 3, 4, 5]
result = [i**2 for i in x]
print(result)   # output: [1, 4, 9, 16, 25]


"""
Conditional statements in list comprehension:
    List comprehensions can include conditional statements to filter or modify items based on specific criteria. 
    These conditionals help us create customized lists quickly and making the code cleaner and more efficient.
"""
# Example: Suppose we want to filter all even list from the given list.
print("\nExample: Conditional statements in list comprehension")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [i for i in x if (i%2 == 0)]
print(even_numbers) # output: [2, 4, 6, 8, 10]

"""
Example: Flattening a list of lists:
    Suppose we have a list of lists and we want to convert it into a single list.
"""
print("\nExample: Flattening a list of lists:n")
lst = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
flattening_lst = [i for row in lst for i in row]
print(flattening_lst)   # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
