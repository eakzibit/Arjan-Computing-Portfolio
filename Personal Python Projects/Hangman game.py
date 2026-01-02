# Author: Arajn Vir Singh
# Date: X
# Program: Hangman
# Version: 1.1
# Updated to capture valid input only
# Comment: This game has adapted 

#import all required libraries and files
import random, Hangaman_template, sys 

#define all functions
def select_word(words): #  This selects a random word from the list in line 30
    return random.choice(words)

def select_word2(words2): #  This selects a random word from the list in line 30
    return random.choice(words2)

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

def get_validate_user_input(): #  This helper function ensures that teh user can only input a single valid character
    guess = input("Guess a letter: ")
    while len(guess) > 1 or not guess.isalpha(): #  This checks if the length of the guess is more than 1
        print("Only single alphabetic letters a-z are allowed. Please input a validate letter")
        guess = input("Guess a letter: ")
    return guess

def guess_letters(guess, secret_word): # This function checks if the users input is part of the word
    if guess in secret_word: # This if statement will return True if the guess is in the word
        return True
    else:
        return False

def get_dictionary():
    import pandas as pd
    url = "hangman_dict.csv"
    df  = pd.read_csv(url)
    words = df['word'].tolist()
    words = [s.lower() for s in words]
    return words

#instantiate variables
words=["tax","death","happiness","chair","python","sweet","xenophobia"]
words2 = get_dictionary()
remaining_guesses= 5
guessed_letters = ""
#secret_word = select_word(words)
secret_word = str(select_word2(words2))

guess = ""

#Game
print("Welcome to Arjan's hangman game :)\n") 
while remaining_guesses > 0 and len(guessed_letters) < len(get_unique_letters(secret_word)): # This is the game loop
        
    guess = get_validate_user_input()
    guess_in_secret_word = guess_letters(guess, secret_word)
    print(guess,"in main while body")
    if guess_in_secret_word: # This checks if the function returns True 
     if guess in guessed_letters: # This checks if the guess is already inside the word
        print("you have already guessed the letter {}".format(guess))
     else:
        print("YIPPEEEEE {} was part of the word ●◡●".format(guess))
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
     print("NOOOOOOO you lost :( \n The word was",secret_word)








