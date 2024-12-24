"""
match Statements:
    A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. 
    
    This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), 
    but it’s more similar to pattern matching in languages like Rust or Haskell

    Only the first pattern that matches gets executed and it can also extract components (sequence elements or object attributes) from the value into variables.

"""
# For Example:
x = 10

match x:
    case 10:
        print("It is 10")   # It is 10
    case 20:
        print("It is 20")
    case _:
        print("It's neither 10 nor 20")
    