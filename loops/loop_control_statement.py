"""
Loop Control Statements:
    Loop control statements change execution from their normal sequence. 
    When execution leaves a scope, all automatic objects that were created in that scope are destroyed. 
    
    Python supports the following control statements.
    1. Continue Statement: as the name suggest, it skip the current iteration and continue with the next iteration.  
    2. Break Statement: The break statement in Python brings control out of the loop. 
    3. Pass Statement: We use pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.
"""
# For Example:   

# Continue Statement:
print("\Continue Statement")
for letter in "Nishan":
    if (letter == 's'):
        continue
    print(letter)

"""
Output:
N
i
h
a
n
"""

# Break Statement:
print("\nBreak Statement")
for letter in "Nishan":
    if (letter == 's'):
        break
    print(letter)

"""
Output:
N
i

"""

# Pass Statement:
print("\Pass Statement")
for letter in "Nishan":
    pass
    print(letter)

"""
Output:
N
i
s
h
a
n
"""