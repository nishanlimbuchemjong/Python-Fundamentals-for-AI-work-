"""
Python Inheritance:
    Inheritance allows a class (child class) to acquire properties and methods of another class (parent class).
    It supports hierarchical classification and promotes code reuse.

Types of Inheritance:
    Single Inheritance: 
        A child class inherits from a single parent class.
    Multiple Inheritance: 
        A child class inherits from more than one parent class.
    Multilevel Inheritance:
        A child class inherits from a parent class, which in turn inherits from another class.
    Hierarchical Inheritance: 
        Multiple child classes inherit from a single parent class.
    Hybrid Inheritance: 
        A combination of two or more types of inheritance.

"""
# For Example:

# Base class:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} make a sound")

# Single Inheritance
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed
    def speak(self):
        print(f"{self.name} barks")

# Multiple Inheritance
class Pet:
    def __init__(self, owner):
        self.owner = owner

class Cat(Dog, Pet):
    def __init__(self, name, breed, owner):
        Dog.__init__(self, name, breed)
        Pet.__init__(self, owner)

    def speak(self):
        print(f"{self.name} meows")
            
# Multilevel Inheritance
class Puppy(Dog):
    def __init__(self, name, breed, age):
        Dog.__init__(self, name, breed)
        self.age = age
    def speak(self):
        print(f"{self.name} wags its tail")

# Hierarchical Inheritance
class Tiger(Animal):
    def __init__(self, name, habitat):
        Animal.__init__(self, name)
        self.habitat = habitat
    
    def speak(self):
        print(f"{self.name} roars")

# Hybrid Inheritance (combination of multiple and multilevel)
class Hybrid(Dog, Tiger):
    def __init__(self, name, breed, habitat):
        Dog.__init__(self, name, breed)
        Tiger.__init__(self, name, habitat)

    def speak(self):
        print(f"{self.name} makes a hybrid sound")


# Create objects of different classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese", "Alice")
puppy = Puppy("Rocky", "Labrador", 1)
tiger = Tiger("Sheru", "Jungle")
hybrid = Hybrid("Tiggy", "Crossbreed", "Forest")

# Calling speak() method of each class
dog.speak()      # Buddy barks
cat.speak()      # Whiskers meows
puppy.speak()    # Rocky wags its tail
tiger.speak()    # Sheru roars
hybrid.speak()   # Tiggy makes a hybrid sound