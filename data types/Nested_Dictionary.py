"""
Nested Dictionary:
    A Dictionary in Python works similarly to the Dictionary in the real world. 
    The keys of a Dictionary must be unique and of immutable data types such as Strings, Integers, and tuples, 
    but the key values can be repeated and be of any type.

    In simple form, Nesting Dictionary means putting a dictionary inside another dictionary. 

Creating a Nested Dictionary:
    Nested dictionary can be created by placing the comma-separated dictionaries enclosed within braces. 

"""
# For Example:
nested_dict = {'name': {'first_name': 'Nishan', 'last_name': 'Limbu'},
                'phone': {'ncell': '9803912433'}
                }
print(nested_dict)      # output: {'name': {'first_name': 'Nishan', 'last_name': 'Limbu'}, 'phone': {'ncell': '9803912433'}}


"""
Adding Elements to a Nested Dictionary:
    The addition of elements to a nested Dictionary can be done in multiple ways:
    i. One way to add a dictionary in the Nested dictionary is to add values one be one, Nested_dict[dict][key] = ‘value’. 
    ii. Another way is to add the whole dictionary in one go, Nested_dict[dict] = { ‘key’: ‘value’}.
"""
# For Example:
dict ={}
dict['dict1'] = {}

# Adding elements one at a time
dict['dict1']['name'] = "Nishan"
dict['dict1']['age'] = 24
print("After adding dictionary 'dict1':\n")
print(dict)     # output: {'dict1': {'name': 'Nishan', 'age': 24}}

#  Adding whole dictionary:
dict['dict2'] = {'name': 'Anu Limbu', 'age':28, 'phone': '9804587326'}
print("\nAfter adding dictionary 'dict2':\n")
print(dict)     # output: {'dict1': {'name': 'Nishan', 'age': 24}, 'dict2': {'name': 'Anu Limbu', 'age': 28, 'phone': '9804587326'}}


"""
Access Elements of a Nested Dictionary:
    In order to access the value of any key in the nested dictionary, we use indexing [] syntax.
    
"""
# For Example:
nest_dict = {'dict1': {'name': 'Nishan', 'age': 24}, 
            'dict2': {'name': 'Anu Limbu', 'age': 28, 'phone': '9804587326'}
            }
# Printing value corresponding to key 'name' in dict1:
print(nest_dict['dict1']['name'])   # output: Nishan

# Printing value corresponding to key 'age' in dict2:
print(nest_dict['dict2']['age'])    # output: 28


"""
Deleting Dictionaries from a Nested Dictionary:
    Deletion of dictionaries from a nested dictionary can be done either by using the 'del' keyword or 
    by using pop() function.
"""
# For Example:
nest_dict1 = {'dict1': {'name': 'Nishan', 'age': 24}, 
            'dict2': {'name': 'Anu Limbu', 'age': 28, 'phone': '9804587326'}
            }

# Deleting dictionary using 'del' keyword
del nest_dict1['dict2']
print("After deleting: \n")
print(nest_dict1)       # output: {'dict1': {'name': 'Nishan', 'age': 24}}

 
# Deleting dictionary using pop function:
nest_dict1.pop('dict1')
print("After deleting: \n")
print(nest_dict1)       # output: {}