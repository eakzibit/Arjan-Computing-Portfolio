username=input("what is your username? ")
password=input("what is your password? ")
if len(password) < 6:                       #This if statment will detect if the password is smaller than 6 digits
    print ("invalid your password is less than six characters")
thirdletter=input("what is the third letter of your password")
if thirdletter==password[2]:                 #This if statment detects if the third letter is the third letter of the users  password.
    print("you may now proceed to the next step")
else:
    print("incorrect details")
sixthletter=input("what is the sixth letter of your password")
if sixthletter==password[5]:                #This if statment detects if the sixth letter is the sixth letter of the users password.
    print("you may now proceed ")
else:
    print("incorrect details")


