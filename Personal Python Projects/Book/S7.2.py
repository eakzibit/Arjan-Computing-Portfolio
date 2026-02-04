names1=input("what is your 1st team name ") # Next 3 lines input a team name
names2=input("what is your 2nd team name ")
names3=input("what is your 3rd team name ")
names4=input("what is your 4th team name ")
Names=[names1,names2,names3,names4] # This puts the variables in a list
for i in range (3): #  This loop repeats 3 times, because only 1 team can win
 x=input("what team do you want to get rid of? ")
 Names.remove(x) # This removes  the team from your input above from your list
 print(Names) #  this pritns out a list

print("WE HAVE A WINNER",Names,"is our winner ") # This prints out the final team
