print("hello, world")
# Syntax error, error  de sintaxis
# valueError, error de tipo de dato en variables
# try:
#     x = int(input("What's x? "))
#     print (f"x is {x}")
# except ValueError:
#     print("x is not integer")

# NameError: problem with the names of varieables
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not integer")
# else: #Executes if no error was found
#     print (f"x is {x}")

#
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not integer")
#     else: #Executes if no error was found
#         break

# print (f"x is {x}")

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not integer")

# main()

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass #Mecanismo para no hacer nada durante el error
main()