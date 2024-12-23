"""
2. Global Variable:
    Variables defined outside any function are global 
    and can be accessed inside functions using the global keyword.
"""
# For Example:

# function for greeting
greet = "I am greeting"
def greeting():
    global greet
    greet = "Hello"
    print(greet)

# calling the function
greeting()

print(greet)