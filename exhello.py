print("hello, world")
# Syntax error, error  de sintaxis
# valueError, error de tipo de dato en variables
try:
    x = int(input("What's x? "))
    print (f"x is {x}")
except ValueError:
    print("x is not integer")