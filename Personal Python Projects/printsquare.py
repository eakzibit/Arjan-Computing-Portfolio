
sizeofsquare=int(input("please enter size:")) # This inputs the size of the square
solidline="" # Create two empty variables 
edgeline=""
no_edgelines= sizeofsquare-2


for i in range(0,sizeofsquare): #  This i in range adds a # to the empty solidline variable
    solidline+="# "
    if i==0:
        edgeline+="#"
    elif i<sizeofsquare-1:  # This detects of i is creater than the size of square - 1 and if it is, it will create a gap inbetween the square, and it will repeat this until i is less than the size of square
        edgeline+="  "
    else:
        edgeline+=" #"
for i in range(0,sizeofsquare): #  This prints the square
    if i==0:
        print(solidline)
    elif i<=no_edgelines:
        print(edgeline)
    else:
        print(solidline)
