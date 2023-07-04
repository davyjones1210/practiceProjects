from cryptography.fernet import Fernet
#This module allows you to encrypt text

#Using a key, a string of text you cannot get back without knowing the key
#key + password + text of encrypt = random text

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)



def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User: " + user + " | " + "password: " + fer.decrypt(passw.encode()).decode())
def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



while True:
    mode = input("Would you like to add a new password or view existing ones (view or add)? (Enter 'q' to quit) ").lower()

    if mode == "q":
        break


    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue



