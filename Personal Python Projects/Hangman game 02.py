# Author: Arajn Vir Singh
# Date: X
# Program: Hangman
# Version: 0.2
# Updates: Replaced sys.exit on input failure with retry logic
# Comment: This game has adapted X X ADSASDFSAF

#import all required libraries and files
import random, Hangaman_template, sys 

#define all functions
def select_word(words): #  This selects a random word from the list in line 30
    return random.choice(words)

def print_secret_word(secret_word, guessed_letters): # This checks how many guessed letters there are 
    for letter in secret_word:
        if letter in guessed_letters: #  This checks if the letter is in the right place
            print("{}".format(letter), end="") # This prints the right letter in the right place
            # {} is the letter 
        else:
             print(" _ ", end="") # This does nothing
    print("\n")

def get_unique_letters(word):
    return"".join(set(word))

def guess_letters(guess, secret_word): # This is the guessing system
    if len(guess) > 1 or not guess.isalpha(): #  This checks if the length of the guess is more than 1
       # print(" Unable to continue...")
       # sys.exit() # This ends the game
       print("Only single letters are allowed. Please try again!")

       guess=""
       print(guess,"AFTER reset")
       guess = input("Guess a letter ")
       print(guess, "latest guess")
       return guess_letters(guess, secret_word)
       print(guess,"NEVER GETS HERE")
    else:
        if guess in secret_word: # This nested if statement will return True if the guess is in the word
            return True
        else:
            return False

#instantiate variables
words=["tax","death","happiness","chair","python","sweet","xenophobia"]
remaining_guesses= 5
guessed_letters = ""
secret_word = select_word(words)
guess = ""

#Game
print("Welcome to Arjan's hangman game :)\n") 
while remaining_guesses > 0 and len(guessed_letters) < len(get_unique_letters(secret_word)): # This is the game loop
    guess = input("Guess a letter:")
    print(guess,"before gisw")
    guess_in_secret_word = guess_letters(guess, secret_word)
    print(guess,"before gasw")
    print(guess_in_secret_word,"letter coming out of cuntion")
    if guess_in_secret_word: # This checks if the function returns True 
     if guess in guessed_letters: # This checks if the guess is already inside the word
        print("you have already guessed the letter {}".format(guess))
     else:
        print("YIPPEEEEE ", guess, " was part of the word ●◡●".format(guess))
        guessed_letters += guess
    else: # If the function returns False it will remove one of our guesses
     print("NOOPPPEE {} isnt in there =C".format(guess))
     remaining_guesses -= 1

    print(Hangaman_template.get_hangman_stage(remaining_guesses)) # This will print the hangman art from the template
    print("\n{} attempts remaining\n".format(remaining_guesses)) # Print the remaining guesses
    print_secret_word(secret_word, guessed_letters) 
    print("\n\nNumber of letters guessed: {}\n".format(len(guessed_letters))) # This will print the amount of letters guessed

#This is the win check
if sorted(guessed_letters)  == sorted(get_unique_letters(secret_word)): # The sorted function ensures that both string are correctly ordered for comparison
    print("YESSSSSS YOU WON :)")
else:
     print("NOOOOOOO you lost :( \n")

