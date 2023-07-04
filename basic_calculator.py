#define the functions needed: add, sub, mul, div
#print options to the user
#ask for values
#call the functions
#while loop to continue the program


def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mult(a,b):
    answer = a * b
    print(str(a) + " x " + str(b) + " = " + str(answer))

def div(a,b):
    answer = a/b
    print(str(a) + " / " + str(b) + " = " + str(answer))

while True:


    print("Welcome to the calculator.")
    print("Please choose from the options below")
    print("A: Addition")
    print("B: Subtraction")
    print("C: Multiplication")
    print("D: Division")
    print("E: Exit")

    choice = input("Input your choice: ")

    if choice.lower() == "a":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a,b)
    elif choice.lower() == "b":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a,b)
    elif choice.lower() == "c":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mult(a,b)
    elif choice.lower() == "d":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        div(a,b)

    elif choice.lower() == "e":
        print("Program ended")
        quit()
