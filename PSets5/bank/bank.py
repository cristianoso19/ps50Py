def main():
    greeting = input("Grettig: ")
    amount = value(greeting)
    print(amount)


def value(greeting):
    greeting = greeting.strip().lower().capitalize()

    if greeting.startswith("Hello"):
        return 0
    elif greeting.startswith("Hey") or greeting.startswith("How"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()