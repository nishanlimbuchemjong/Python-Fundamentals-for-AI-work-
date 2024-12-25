"""
Writing to a File:
    Writing to a file is done using file.write() which writes the specified string to the file. If the file exists, its content is erased. 
    If it doesn’t exist, a new file is created.
"""
# For Example: Writing to a File in Write Mode (w)
file = open('write_file.txt', 'w')
file.write("Hello, This is my new file called write_file.txt which is auto created")
file.close()

"""
Output:


"""
