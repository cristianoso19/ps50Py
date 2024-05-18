import sys
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(sys.argv) <= 3 and sys.argv[1] == "-f":
        try:
            font = sys.argv[2]
            figlet.setFont(font=font)
            message = input("Input: ")
            print(figlet.renderText(message))
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
        
main()

