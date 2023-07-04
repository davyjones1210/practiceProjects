#collect email address from user
#split the email using @ delimiter
#Print username, domain name, further split it using . delimiter

def main():
    print("Welcome to the email address slicer")
    print("")
    email_input = input("Enter your email address: ")
    (username, domain) = email_input.split("@")
    (domain_name, extension) = domain.split(".")
    print("Username: ", username)
    print("Domain name: ", domain_name)
    print("Extension: ", extension)

main()





