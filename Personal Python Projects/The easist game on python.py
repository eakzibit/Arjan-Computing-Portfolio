print("You are in the street, you see an alleyway.\n")  
C1 = int(input("1: Go into the alleyway or 2: Don't go into the alleyway \n"))  

if C1 == 1:  
    print("You see a door.")  
    C1A = int(input("1: Enter the door or 2: Don't enter the door \n"))
    if C1A == 1:  
        print("You entered a Russian base.")  
        C1B = int(input("1: Climb into the vents or 2: Wear a suit \n"))
    else:  
       print("An aeroplane sweeps down, and out steps TOM CRUISE!?")  
       print("+++++++++++ENDING: Tom Cruise++++++++++")  
    if C1B == 1:  
            print("There is a split path.")  
            C1C = int(input("1: Right or 2: Left \n"))  
            if C1C == 2:  
                print("You see a demagargoon.")  
                E1 = int(input("1: Kill the demagargoon or 2: Speak to the demagargoon \n"))  
            else:
                print("the fans chop you into tiny pieces")
                print("+++++++++++Ending:Death++++++++++++")
                if E1 == 1:  
                    print("+++++++++ENDING: Demagargoon ++++++++++")  
                else:  
                    print("+++++++++ENDING: Death++++++++++")  
    else:  
            print("+++++++++ENDING: Death++++++++++")  

if C1 == 2:
    C2 = int(input("1: Order a burger or 2: Don't: "))
    
    if C2 == 1:
        print("The burger you ate had chemicals that turned you into burger-man!")
        print("BANG!!!! Your enemy CHARLIE CHEESE IS OUTSIDE!")
        
        C2A = int(input("1: Go outside and confront him or 2: Don't be bothered: "))
        
        if C2A == 1:
            print("You fight for hours until you pin him on the ground.")
            E2 = int(input("1: Spare him or 2: KILL HIM"))
            
            if E2 == 1:
                print("You spare Charlie Cheese, but he stabs you with a tiny knife.")
                print("++++++++++++++Ending: Death ++++++++++++++")
            else:
                print("You defeat Charlie Cheese and realize what you've done.")
                print("++++++++++++++Ending: Are you really a hero? ++++++++++++++")
        else:
            print("You decide to ignore Charlie Cheese.")
            print("++++++++++++++Ending: HATED ++++++++++++++")
    else:
        print("++++++++++++++Ending: Sad :( ++++++++++++++")
