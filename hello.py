name = input("What's your name? ").strip().title()

# split user's name into first name and last name
first, last = name.split(" ")

#Remove whitespace from str and capitallize 
#name = name.strip().title() #method

print(f"hello, {first}") #Py new feature f string