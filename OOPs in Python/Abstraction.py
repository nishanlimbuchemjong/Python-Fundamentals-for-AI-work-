"""
Data Abstraction in Python:
    Data abstraction is one of the fundamental concepts of Object-Oriented Programming (OOP). 
    It is the process of hiding the implementation details from the user and exposing only the necessary functionality.

    In Python, we can implement data abstraction using abstract classes and abstract methods, 
    which can be done using the abc (Abstract Base Class) module.

Concepts of Data Abstraction:
    Abstract Class: 
    A class that cannot be instantiated on its own and is used as a base for other classes. 
    It can have abstract methods, which are methods that do not have any implementation in the abstract class 
    and must be implemented by subclasses.

    Abstract Method: 
    A method that is declared but contains no implementation. 
    It must be implemented by the subclasses of the abstract class.
"""
# For Example:
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    def sleep(self):
        print("Sleeping .....")

class Dog(Animal):
    # implementing the abstract method 'sound'
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    # implementing the abstract method 'sound'
    def sound(self):
        print("Cat meows")

# Create objects of the subclasses
dog = Dog()
cat = Cat()

# Call the methods
dog.sound()  # Output: Dog barks
cat.sound()  # Output: Cat meows

# Call the concrete method from the base class
dog.sleep()     # Output: Sleeping ....
cat.sleep()     # Output: Sleeping ....

