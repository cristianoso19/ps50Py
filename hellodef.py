def main():
    hello() #Call to function with no arguments
    name = input("What's your name? ")
    hello(name)

def hello(to="world"): # to="WORLD" is default value of parameter
    print("hello, ", to) #The identetion is very important!
#Scope: the variable exists only int the function where it is created

main() #call the main function in the bottom 
 