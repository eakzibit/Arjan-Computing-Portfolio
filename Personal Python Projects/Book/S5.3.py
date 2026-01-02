import time


word=input("what is your message? ") # This inputs a message
wordoutput="" # The reason this is blank is because the letters will be added onto it in line 8
word=word.upper()
for letter in word: # This will count the letters and repeat that many times
    wordoutput = wordoutput+letter
    time.sleep(1)# This counts a second before looping again       
    print(wordoutput)
    













