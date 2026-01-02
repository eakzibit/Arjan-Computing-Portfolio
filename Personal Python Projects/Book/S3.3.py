speedlim=int(input("what is the mph? "))
dist=int(input("what is the distance? "))
time=int(input("what is the time taken in hours? "))
averagespeed= dist/time# This calculates the average speed
print(averagespeed)
print("has the speed limit been broken?")
print(averagespeed>speedlim) # This will print either True or False as it is a boolean
    
