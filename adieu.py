import inflect

def main():
    p =  inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ") 
            names.append(name)
        except EOFError: #Catch Ctrl-D
            break
        except:
            print("An error was found")

    print("Adieu, adieu, to ", p.join(names))

main()