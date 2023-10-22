
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    #return (n % 2 == 0) # Return what happen in parentesis, just return the question
    return n % 2 == 0 #  You dont need the parentesis just return the question
    
main()