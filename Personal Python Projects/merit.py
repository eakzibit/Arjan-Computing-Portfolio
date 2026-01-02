def meritChecker(merits, demerits):
 totm=merits-demerits
# print(totm)
 if totm<=19:
    print(name,"needs a talking to")
 if totm>=20 and totm<=44:
     print(name,"gets a free lunch token")
 if totm>=45 and totm<=99:
    print(name,"gets an afternoon of boardgames")
 if totm>=100:
    print(name,"gets a LED KEYBOARD")


name=input("what is the name of the student: ")
merits=int(input("how many merits did they get: "))
demerits=int(input("what is the amount of demerits: "))
meritChecker(merits,demerits)



#These are my test cases to make sure the logic is working correctly
#print("Starting Test 1: input 50,40")
#meritChecker(50,40) #expected output: needs talking to
#print("Starting Test 2: input 80,40")
#meritChecker(80,40) #expect token)
#print("Starting Test 3: input 100,50")
#meritChecker(100,50)#expect boardgame and token
#print("Starting Test 4: input 120,10")
#meritChecker(120,10)#expect keyboard, boardgame, token


