from random import randint


def main():
    level = get_level("Level: ")
    num1 = generate_integer(level)
    num2 = generate_integer(level)
    hit = False
    tries = 0
    message = f"{num1} + {num2} = " 
    response = 0
    while hit == False:
        if tries == 3:
            print(message, num1+num2, sep="")
            break
        else:
            tries += 1
            try:
                response = int(input(message))
            except ValueError:
                print("EEE")
        
            if response == num1+num2:
                hit = True 
        

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