"""
Python Polymorphism:
    Polymorphism allows methods to have the same name but behave differently based on the object’s context. 
    It can be achieved through method overriding or overloading.

    Types of Polymorphism:
        1. Compile-Time Polymorphism: 
            This type of polymorphism is determined during the compilation of the program. 
            It allows methods or operators with the same name to behave differently based on their input parameters or usage. 
            It is commonly referred to as method or operator overloading.

        2. Run-Time Polymorphism: 
            This type of polymorphism is determined during the execution of the program. 
            It occurs when a subclass provides a specific implementation for a method already defined in its parent class, commonly known as method overriding.
      
"""
# For Example: Runtime Polymorphism (Method Overriding)
class Animal:
    def sound(self):
        return "Animal makes sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"

# Demonstrating Runtime Polymorphism
animals = [Dog(), Cat(), Animal()]

print("Example of Runtime Polymorphism (Method Overriding):")
for animal in animals:
    print(animal.sound())


"""
Output:
    Bark
    Meow
    Animal makes sound
"""


# For Example: CompileTime Polymorphism (Method Overloading)
class Calculate:
    def calculation(self, length, breadth=None, height=None):
        if ((breadth is None) and (height is None)):
            return length**2
        elif (height is None):
            return length * breadth
        else:
            return length * breadth * height

# Create an object of the Calculate class
cal = Calculate()

# Demonstrating Compile-time Polymorphism
print("\nExample of CompileTime Polymorphism (Method Overloading):")
print("Area of square:", cal.calculation(5))  
print("Area of rectangle:", cal.calculation(5, 10)) 
print("Volume of cuboid:", cal.calculation(5, 10, 15)) 

"""
Output:
    Area of square: 25
    Area of rectangle: 50
    Volume of cuboid: 750

"""
