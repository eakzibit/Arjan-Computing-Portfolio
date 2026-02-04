#-----------------------------------------------------------------------------To do list---------------------------------------------------------------------------------#

import sys


#Create an empty list

list=[]

#Create an empty variable for menu

menu = 0

#Create an while loop


def start_up():
 menu= int(input("What would you like to do today? \n 1: Add an item \n 2: Remove an item \n 3: See list \n 4 Exit \n "))
 if menu == 1:
   item=str(input("What item would you like to add ")) 
   list.append(item)
   print(list)
 elif menu == 2:
   print(list)
   remove=int(input("What number would you like to remove"))
   if remove <= 0 or remove >= list:
                print("Please input a valid argument")
                remove=int(input("What number would you like to remove"))
   remove = remove-1
   del list[remove]
 elif menu ==3 :
   print(list)
 elif menu == 4:
   sys.exit
 else:
    menu= int(input("What would you like to do today? \n 1: Add an item \n 2: Remove an item \n 3: See list \n 4 Exit \n "))
 return menu






def loop():
 while menu >= 4 :
  menu= int(input("What would you like to do today? \n 1: Add an item \n 2: Remove an item \n 3: See list \n 4 Exit \n "))
 if menu == 1:
  item=str(input("What item would you like to add ")) 
  list.append(item)
  print(list)
 elif menu == 2:
    print(list)
    remove=int(input("What number would you like to remove"))
    remove = remove-1
    del list[remove]
 elif menu ==3 :
     print(list)
 elif menu == 4:
   sys.exit
 else:
      menu= int(input("What would you like to do today? \n 1: Add an item \n 2: Remove an item \n 3: See list \n 4 Exit \n "))
     


start_up()
loop()
