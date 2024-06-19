import random
import sys

def main():
    level_int = intInput("Level: ")
    rndm = random.randint(1,level_int)
    while True:
        guest = intInput("Guess: ")
        if guest == rndm:
            break
        elif guest > rndm:
            print("Too large!")
        else:
            print("Too small!")

    print("Just right!")
    sys.exit()

def intInput(message):
    while True:
        try:
            int_number = int(input(message))
            if (int_number > 0):
                break
        except:
            pass
    return int_number

main()
