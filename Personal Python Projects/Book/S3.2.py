import random


number=random.randint(1,50)# This creates a random number between 1-50 which is stored in a variable
print("you have two guesses to find the random number between 1,50")
awnser_1= input ("what is your first choice ") #First awnser
awnser_2=input ("what is your second choice ")# Second awnser
if awnser_1 or awnser_2== number: # This if statment will detect if either of the awnsers = the number variable
    print("YOU WIN A CAR")
else:
    print("wommp womp you lose")
print(number)
