"""
Positional Arguments:
    We used the Position argument during the function call so that the first argument (or value) is assigned to name and the second argument (or value) is assigned to age.
"""
# For Example:
def student_detail(name, age):
    print("Name: name}\nAge: {age}\n")

# We will get correct output because argument is given in order
print("Case-1:")
student_detail("Suraj", 27)
"""
Output:
Case-1:
Name: name}
Age: {age}
"""
# We will get incorrect output because argument is not in order
print("\nCase-2:")
student_detail(27, "Suraj")
"""
Output:
Case-2:
Name: name}
Age: {age}
"""