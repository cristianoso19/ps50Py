import sys
import requests

def main():
    i = 0
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit() #terminate program
    else:
        try:
            i = float(sys.argv[1])
        except:
            print("Command-line argument is not a number")
            sys.exit() #terminate program

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        exchange = o["bpi"]["USD"]["rate_float"]
        amount = i*exchange
        print(f"${amount:,.4f}")
    except requests.RequestException:
        print(TypeError)

if __name__ == "__main__":
    main()

