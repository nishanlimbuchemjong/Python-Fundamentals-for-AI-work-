"""
Reading a File:
    Reading a file can be achieved by file.read() which reads the entire content of the file. 
    After reading the file we can close the file using file.close() which closes the file after reading it, which is necessary to free up system resources.

"""
# For Example:
file = open('file_in_out.txt', 'r')
content = file.read()
print("Content: ", content)
file.close()

"""
Output:

Content:  File Handling in Python:
    File handling refers to the process of performing operations on a file such as creating, opening,
    reading, writing and closing it, through a programming interface.

    It involves managing the data flow between the program and the file system on the storage device,
    ensuring that data is handled safely and efficiently.

File Modes in Python:
    r   Read mode. Opens a file for reading. The file must exist.
    w   Write mode. Opens a file for writing. Creates a new file if it doesnâ€™t exist or truncates the file if it exists.
    a   Append mode. Opens a file for appending. Creates a new file if it doesnâ€™t exist.
    b   Binary mode. Opens a file in binary mode.
    t   Text mode. Opens a file in text mode. Default mode.
    x   Exclusive creation mode. Creates a new file and fails if it already exists.
    r+  Read and write mode. Opens a file for both reading and writing. The file must exist.
    w+  Write and read mode. Opens a file for both writing and reading. Creates a new file if it doesnâ€™t exist or truncates the file if it exists.
    a+  Append and read mode. Opens a file for appending and reading. Creates a new file if it doesnâ€™t exist.

Opening a File in Python:
    To open a file we can use open() function, which requires file path and mode as arguments

    Syntax:
        file object = open(<file-name>, <access-mode>, <buffering>)

"""