name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Harmione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: #Default
        print("Who?")