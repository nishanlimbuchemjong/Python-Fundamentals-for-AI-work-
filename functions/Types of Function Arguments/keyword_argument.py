"""
Keyword Arguments:
    The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.

"""
# For Example:
def student_details(first_name, last_name, age, address):
    print("First name: {first_name}\nLast name: {last_name}\nAge: {age}\nAddress: {address}")

# calling the funciton with keyword arguments
student_details(first_name='Nishan', last_name='Limbu', age=24, address='Lalitpur, Nepal')

"""
Output: 
First name: {first_name}
Last name: {last_name}
Age: {age}
Address: {address}

"""