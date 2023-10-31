def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def valid_range(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def valid_first_char(s):
    if s[0:1].isalpha():
        return True
    else:
        return False

def valid_num(s):
    num = ""
    for char in s[2:-1]:
        if char.isnumeric():
            if char == "0" and num == "" :
                return False
            else:
                num += char
        else:
            num = ""

    return True

#Check no number in middle
def valid_string(s):
    num = ""
    for char in s[2:-1]:
        if char.isnumeric():
            num += char
        elif num != "":
            return False
    return True

def is_valid(s):

    if valid_range(s) and valid_first_char(s) and valid_num(s) and valid_string(s):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
