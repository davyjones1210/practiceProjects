#Ask the user if they want to generate a password or not
#If yes, ask for password length
#generate password
#print password
#Exit program if initial response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
print(characters)

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append((random.choice(characters)))

    random.shuffle(password)

    password = "".join(password)

    print(password)

generate_password()

