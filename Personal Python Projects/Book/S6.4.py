oldpassword="what"

notvalid =True

while notvalid: # While notvalid is True  then it will ask you to input a new password
   newpassword=input("what is your new password: ")
   notvalid=False

   if newpassword== oldpassword:          # The whole if statment checks if your Password is too easy to guess for example line 18
    print("New passwordc cant be the same as your old passsword.")
    notvalid=True
   if newpassword== newpassword.lower():
    print("New passwordc cant be all lower.")
    notvalid=True
   if newpassword== newpassword.upper():
    print("New passwordc cant be all upper.")
    notvalid=True
   if len(newpassword)< 8 or len(newpassword)> 16:                #This checks if the password is longer than 16 charecters and less than 8
    print("New passwordc cant be less than 8 characters or more than 16")
    notvalid=True
print("password is fine")
