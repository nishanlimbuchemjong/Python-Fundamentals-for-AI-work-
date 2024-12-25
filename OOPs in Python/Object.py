"""
Python Objects:
    An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

    An object consists of:
        State: It is represented by the attributes and reflects the properties of an object.
        Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
        Identity: It gives a unique name to an object and enables one object to interact with other objects.

"""
# Creating Object
#     Creating an object in Python involves instantiating a class to create a new instance of that class. 
#     This process is also referred to as object instantiation

# For Example:
class Student:
    country = 'Nepal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of Student class
obj = Student("Nishan Limbu", 24)

print(f"Name: {obj.name}\nAge: {obj.age}")  

"""
Output: 

Name: Nishan Limbu
Age: 24

"""
