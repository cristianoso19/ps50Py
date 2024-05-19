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

    print("\nAdieu, adieu, to", p.join(names))

main()