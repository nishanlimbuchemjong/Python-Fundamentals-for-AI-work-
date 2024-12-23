"""
For Loop in Python:
    For loops are used for sequential traversal. For example: traversing a list or string or array etc. 
    In Python, there is “for in” loop which is similar to foreach loop in other languages. 

    Syntax:
        for iterator_var in sequence:
            statement(s)
    It can be used to iterate over a range and iterators.
"""
# For Example:
n = 10
for i in range(1, n):
    print(i)

"""
Output:
1
2
3
4
5
6
7
8
9
"""
print("\n")
# Example with List, Tuple, String, and Dictionary Iteration Using for Loops in Python
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)

"""
Output:
1
2
3
4
5
"""