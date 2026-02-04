import random

def Registeraccount():      # This subroutine asks the user to register an account
    name = input("Hello, before you become a maths wizz what is your Name? ")
    print("Hello", name, "ready to become a times table Wizz?")

def menu():                             # This subroutine is the menu of the game where you can select an option 
    print("\nSelect an option")
    print("1. Free Choice")
    print("2. Random")
    print("3. Quit")

def Freechoice():    # This is a subroutine for the Free choice mode
    number = int(input("What is the times table you want to work on? "))
    for i in range(1, 13):#This repeats 1-12 times
        print("Work out", number, "x", i)     # prints the number x i 
        answer = int(input("Answer: "))
        if answer == number * i:
            print("Correct!")
        else:
            print("Wrong. The correct answer is", number * i)

def Random(): # This is like free choice mode apart from the fact that the computer chooses what times table you practise
    randomint = random.randint(1, 12)
    for i in range(1, 13):
        print("Work out", randomint, "x", i)
        answer = int(input("Answer: "))
        if answer == randomint * i:
            print("Correct!")
        else:
            print("Wrong. The correct answer is", randomint * i)

# Start program
Registeraccount()

while True: #  This while True runs the whole gameloop.
    menu()
    option = input("Option: ")

    if option == "1":
        Freechoice()
    elif option == "2":
        Random()
    elif option == "3":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

    
               
               
              
    
    
        
