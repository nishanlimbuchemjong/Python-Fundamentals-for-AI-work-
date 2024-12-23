"""
Sequence Data Type in Python:
    It is the ordered collection of similar or different Python data types. 
    Sequences allow storing of multiple values in an organized and efficient fashion. 
    
    There are several sequence data types of Python:
    i. String
    ii. List
    iii. Tuple
"""
"""
1. String Data type:
    They are arrays of bytes representing Unicode characters. In Python, there is no character data type Python, 
    a character is a string of length one.
    Strings in Python can be created using single quotes, double quotes, or even triple quotes.

"""
# For Example:
sentence = "Hello, I am Nishan Limbu"
print(sentence) 

# checking data type:
print(type(sentence)) # output: <class 'str'>

# accessing string with index
print(sentence[0])      # output: H
print(sentence[10])     # output: m 
print(sentence[-5])     # output: L
print(sentence[3])      # output: l
print(sentence[-4])     # output: i


"""
2. List Data type:
    They are just like arrays, declared in other languages which is an ordered collection of data. 
    It is very flexible as the items in a list do not need to be of the same type.
    Lists in Python can be created by just placing the sequence inside the square brackets[].
"""
# For Example:
num = []

# list with integer:
num = [1, 2, 4, 5]
print(num)

# list with mixed data type:
x = ["Nishan", "Limbu", 25]
print(x)

# accessing list items:
# In order to access the list items refer to the index number. 
# In Python, negative sequence indexes represent positions from the end of the array. 
y = ["Nishan", "Limbu", 25]
print(y[0])     # output: Nishan
print(y[2])     # output: 25
print(y[-2])    # output: Limbu

"""
2. Tuple Data type:
    Just like a list, a tuple is also an ordered collection of Python objects.
    The only difference between a tuple and a list is that tuples are immutable. 
    Tuples cannot be modified after it is created.

    tuples are created by placing a sequence of values separated by a ‘comma’ 
    with or without the use of parentheses for grouping the data sequence. 
    Tuples can contain any number of elements and of any datatype (like strings, integers, lists, etc.).
"""
# For Example:

t1= ()

t2 = ("Nishan", "Limbu")
print(t2)

# Note – The creation of a Python tuple without the use of parentheses is known as Tuple Packing.

# Accessing Tuple item:
# In order to access the tuple items refer to the index number. 
# Use the index operator [ ] to access an item in a tuple.

t1 = tuple([1, 2, 3, 4, 5])

# accessing tuple items
print(t1[0])    # output: 1
print(t1[1])    # output: 2
print(t1[-2])    # output: 4
print(t1[4])    # output: 5

