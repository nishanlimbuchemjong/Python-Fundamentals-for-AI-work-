"""
Nested Loops in Python:
    Python programming language allows to use one loop inside another loop which is called nested loop. 

    syntax for Nested while loop:
        while expression:
            while expression:
                statement(s)
            statement(s)
    

    syntax for Nested for loop:
        for iterator_var in sequence:
            for iterator_var in sequence:
                statement(s)
            statement(s)

"""
# For Example:
# Nested for loop:
"""
printing the pyramid:
1 
2 3
4 5 6
7 8 9 10

"""
row = 4
start = 1
for i in range(1, row+1):
    for j in range(i):
        
        print(start, end=" ")
        start += 1
        
    print()
