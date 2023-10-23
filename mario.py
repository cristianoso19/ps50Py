def main():
    print_column(3)
    print_row(4)
    
def print_column(height):
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width)
main()