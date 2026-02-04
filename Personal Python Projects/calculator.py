#get user inputs
userinput1=input("Please input your first number?")
userinput2=input("Please input your second number?")
operator=input("Please enter your operator?")

#convert input to numbers
try:
    input1 = int(userinput1)
    input2 = int(userinput2)
    if operator == "x":
        print(input1*input2)
    elif operator == "+":
        print(input1+input2)
    elif operator == "-":
        print(input1-input2)
    elif operator == "/":
        print(input1/input2)
    else:
        print("unknown operator please try again")

except ValueError:
    print("Oops that was not a number")
    

#print output of calculation

print("thank you for your use")







