import time

seconds=int(input("how many seconds"))#This inputs how long the timer is going to be
for i in range(seconds):
    print (seconds)# This prints the seconds
    time.sleep(1) # This is how long in seconds the program has to wait
    seconds-=1  # This minuses 1 of each second
print("RELEASE THE HOUNDS")

