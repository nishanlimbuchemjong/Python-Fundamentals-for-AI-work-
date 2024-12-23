"""
Dictionary Data Type in Python:
    It is a data structure that stores the value in key: value pairs. 
    Values in a dictionary can be of any data type and can be duplicated, 
    whereas keys can’t be repeated and must be immutable.

    A dictionary can be created by placing a sequence of elements within curly {} braces, 
    separated by a ‘comma’.
"""
# For Example:

dic = {1: 'Nishan', 2: 'Limbu', 3: 'Chemjong'}
print(dic)      # output: {1: 'Nishan', 2: 'Limbu', 3: 'Chemjong'}

# creating dictionary using dict() constructor
d2 = dict(a = 'Nishan', b = 'Limbu', c = 'Chemjong')
print(d2)       # output: {'a': 'Nishan', 'b': 'Limbu', 'c': 'Chemjong'}

"""
Accessing Dictionary Items:
    We can access a value from a dictionary by using the key within square brackets or get() method.
"""
# For Example:

dict1 = {"name": "Nishan", 1: "AI Engineer", (1,2):[1, 2, 4]}

# accessing using key:
print(dict1['name'])       # output: Nishan

# accessing using get() method:
print(dict1.get(1))     # output: AI Engineer

"""
Adding and Updating Dictionary Items:
    We can add new key-value pairs or update existing keys by using assignment.
"""
# For Example:
d = {1: 'Nishan', 2: 'Limbu', 3: 'Chemjong'}
# adding a new key-value pair:
d["age"] = 24
print(d)        # output: {1: 'Nishan', 2: 'Limbu', 3: 'Chemjong', 'age': 24}

# updating an existing value:
d[3] = "Nepal"
print(d)        # output: {1: 'Nishan', 2: 'Limbu', 3: 'Nepal', 'age': 24}

"""
Removing Dictionary Items:
    We can remove items from dictionary using the following methods:
    del: remove an item by key.
    pop(): removes an item by key and returns its value.
    clear(): empties the dictionary.
    popitem(): removes and returns the last key-value pair.
"""
# For Example:
print("\nDeleting items from dictionary:")
di = {1: 'Nishan', 2: 'Limbu', 3: 'Chemjong', 4:"Nepal", "age": 24}

# using del to remove item:
del di['age']
print(di)    # output: {1: 'Nishan', 2: 'Limbu', 3: 'Chemjong', 4: 'Nepal'}

# Using pop() to remove an item and return the value
val = di.pop(1)
print(val)    # output: Nishan

# Using popitem to removes and returns the last key-value pair.
key, val = di.popitem()
print(f"Key: {key}, Value: {val}")      # output: Key: 4, Value: Nepal

# Clear all items from the dictionary
di.clear()
print(di)      # output: {}

"""
{}
Iterating Through a Dictionary:
    We can iterate over keys [using keys() method] , values [using values() method] 
    or both [using items() method] with a for loop.
"""
# For Example:
print("\nIterating items from Dictioanry:")
dictionary1 = {1: 'Nishan', 2: 'Limbu', 3: 'Chemjong', 4:"Nepal", "age": 24}

# Iterating over keys
for key in dictionary1.keys():
    print(key)  
    # output: 1
    # 2
    # 3
    # 4
    # age


# Iterating over values:
for value in dictionary1.values():
    print(value)
    # output:
    # Nishan
    # Limbu
    # Chemjong
    # Nepal
    # 24

# Iterating over key-value pairs:
for key, value in dictionary1.items():
    print(f"key: {key}, Value: {value}")
    # output:
    # key: 1, Value: Nishan
    # key: 2, Value: Limbu
    # key: 3, Value: Chemjong
    # key: 4, Value: Nepal
    # key: age, Value: 24