"""
Anonymous Functions in Python (Lambda Functions):
    In Python, anonymous functions are functions that are defined without a name. 
    These are often called lambda functions because they are created using the' lambda' keyword. 
    They are used for short, simple operations where defining a full function with def might be unnecessary.

    Syntax:
        lambda arguments: expression
"""
# For Example: Basic Lambda Function
print("\nBasic Lambda Funciton Example:")
square = lambda x: x **2
print(square(10))   # output: 100

# For Example: Lambda Function with Two Arguments
print("\nExample of Lambda Function with Two Arguments:")
sum = lambda a, b: a+b
print(sum(10, 20))   # output: 3

"""
Use Cases of Lambda Functions:
    1. Short-Lived Functions: Lambda functions are perfect for tasks where defining a full function is unnecessary.

    2. Used with Higher-Order Functions: Lambda functions are often used as arguments to functions like map(), filter(), and sorted().

"""
# For Example: With map():
print("\nExample of Lambda Function with map():")
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(list(squares))    # output: [1, 4, 9, 16]

# For Example: With filter():
print("\nExample of Lambda Function with filter():")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x%2 == 0, numbers)
print(list(even_numbers))   # output: [2, 4, 6, 8, 10]

# For Example: With sorted():
"""
The sorted() function is used to sort elements like lists, tuples, or other iterable objects. By default, it sorts in ascending order.
Syntax:
    sorted(iterable, key=None, reverse=False)

    where
        iterable: The sequence to be sorted (like a list or tuple).
        key: A function (like a lambda) that specifies the sorting criteria.
        reverse: If True, sorts in descending order.
"""
print("\nExample of Lambda Function with sorted():")
words = ["apple", "banana", "kiwi", "cherry"]
numbers = [5, 2, 8, 1, 3]
points = [(2, 5), (1, 2), (4, 1)]
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 23}
]
print("original data:")
print("Words: ", words)
print("Numbers: ", numbers)
print("Point: ", points)
print("Students: ", students)

print("\nAfter sortind data:")
sorted_word = sorted(words, key=lambda word: len(word))
print("Sorted word: ", sorted_word) # output: Sorted word:  ['kiwi', 'apple', 'banana', 'cherry']

sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted numbers: ", sorted_numbers)       # output: [1, 2, 3, 5, 8]

sorted_point = sorted(points, key=lambda point: point[0])
print("Sorted points: ", sorted_point)       # output: [(1, 2), (2, 5), (4, 1)]

sorted_students = sorted(students, key=lambda stu: stu['age'])
print("Sorted students: ", sorted_students)       # output: Sorted students:  [{'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]

