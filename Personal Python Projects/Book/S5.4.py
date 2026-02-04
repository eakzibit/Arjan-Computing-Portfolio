word="props"
length=len(word) # This counts the amount of leters in the word
print("the word is a",length,"letter word")
for i in range(0,length,2):   # This for loop controlls how many chances you get
    print("Letter", i+1, "is",word[i]) # This prints out 3 words
guess=input ("what is the awnser? ")
if guess == word: # This if statement tells us ifthe awnser is right or not
    print("YOU WIN")
else:
    print("WOMP WOMP YOU LOSE")
