print("welcome to my game! ")
print("Player 2 please look away")
word=input("Player 1 what is your word: ").lower()
for i in range(50):
    print("\n")
print("Player 2 can  now look")
guess=""
numberofguess=0
while guess!= word:
    
    letter=input("Guess a letter ").lower()
    
    if len(letter) > 1:
        print("only one letter please")
    else:
       numberfound=word.count(letter)
       print("it has",numberfound,"letters in it")
       guess=input ("Guess a word ").lower()
       numberofguess=numberofguess+1
       
       if guess != word:
            print("wrong")

print("CONGRATULATIONS you took", numberofguess,"Guesses")
