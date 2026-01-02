import random  

contenders=[]  # Create an empty list to add all the contesters
name=""  
while name!="Draw": # This will ensure that the programme will continue going until the name draw has been inputed
 name=input("please add name")
 if name!="Draw":
     contenders.append(name) # This adds the name to the list
print(contenders)
winner=random.randint(len(contenders)) # This picks a random name from contenders
print("the winner is ", contenders[winner])
