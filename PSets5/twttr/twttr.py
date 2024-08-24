def main():
    original_input = input("Input: ")
    print("Output:", shorten(original_input))

def shorten(word):
    less = ""
    for letter in word:
        if isVowel(letter) == False:
            less += letter
    return less

def isVowel(letter):
    match letter:
        case "a" | "e" | "i" | "o" | "u":
            return True
        case "A" | "E" | "I" | "O" | "U":
            return True
        case _:
            return False

if __name__ == "__main__":
    main()