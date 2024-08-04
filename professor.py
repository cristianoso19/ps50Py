from random import randint

def main():
    score = 0
    level = get_level()

    for i in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        message = f"{num1} + {num2} = "
        tries = 0
        response = 0

        while True:
            if tries == 3:
                print(message, num1+num2, sep="")
                break
            else:
                tries += 1
                try:
                    response = int(input(message))
                    if response == num1+num2:
                        score += 1
                        break
                    else:
                        raise ValueError
                except (ValueError, NameError):
                    print("EEE")

    print("Score:", score)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    range_start =  (10**(level-1))-1 if level == 1 else 10**(level-1)
    range_end = (10**level)-1
    return randint(range_start, range_end)

if __name__ == "__main__":
    main()
