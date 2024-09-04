def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
        except:
            pass
        else:
            break
    print(gauge(percentage))

def convert(fraction):
    x,y = fraction.split("/")
    x,y = int(x), int(y)
    if y==0:
        raise ZeroDivisionError
    elif y<x:
        raise ValueError
    return round(x/y*100)

def gauge(percentage):
    if percentage <= 1:
        result = "E"
    elif percentage >= 99:
        result = "F"
    else:
        result = str(percentage)+"%"
    return result

if __name__ == "__main__":
    main()