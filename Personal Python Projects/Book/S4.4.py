
number=52 # This is the number that is going to be guessed
for i in range(10):  # This for loop will stop after 10 guesses 
    guess=int(input("what is your guess"))
    if guess<number:       # This will see if the number is too low
       print("too low")
       print("did you get within ten",guess>=42) 
    if guess>number:# This will see if the number is too high
       print("too high")
       print("did you get within ten",guess<=62)
    if guess==number:  # This sees if the number is the same as the variable
       print("you win")
       break #<--- this exits the for loop
