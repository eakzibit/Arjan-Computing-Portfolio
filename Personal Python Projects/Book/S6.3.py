mastercode= "C41llw4rE 5tUd10" #  This is the master code
pcode=input("what is your code? ") #  this is the input dor the password
print("the alarm will go into a test mode please stay calm ")
goingoff=input("WHAT IS THE PASSWORD ")  #This inputs the password
off=True  # Initialise a boolean variable
while off==True: # While off is true the  if statement will check if the password is correct 
    if goingoff==pcode or goingoff==mastercode:   # This checks if the input is equal to the master code or the normal code.
     print("test run complete chillware studios we ensure your saftey...")
     off=False # this ends the loop
    else:
     print("wrong password we are contacting the police")
     goingoff=input("WHAT IS THE PASSWORD")

# Here is another way I tried to do it



#while pcode!=goingoff or mastercode!=goingoff:
#    print("wrong password we are contating the police")
 #   goingoff=input("WHAT IS THE PASSWORD")
#print("test run complete chillware studios we ensure your saftey...")
