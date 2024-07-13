from random import randint


def main():
    level = get_level("Level: ")
    num1 = generate_integer(level)
    num2 = generate_integer(level)
    print(num1, num2)
def get_level(message):
    while True:
        try:
            int_number = int(input(message))
            if (1 <= int_number <= 3):
                break
        except:
            pass
    return int_number 

def generate_integer(level):
    range_start = 10**(level-1)
    range_end = (10**level)-1
    return randint(range_start, range_end)

if __name__ == "__main__":
    main()