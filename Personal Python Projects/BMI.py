i=0
while i==0:
  weight=float(input("what is your weight in KG? "))
  if weight>250 or weight<=0:
       print("ERROR PLEASE ENTER BETWEEN 0-250")
  else:
       i=1
  

c=0
while c==0:
    height=float(input("what is your height in M? "))
    if height>4 or height<=0:
        print("ERROR PLEASE ENTER BETWEEN 1-4")
    else:
         c=1



BMI=weight/(height**2)
BMI2=round(BMI,2)
print(BMI2)
if BMI2< 18.5:
    print("You are underweight")
elif BMI2<29.9:
    print("You are a normal weight")
elif BMI2<34.9:
    print("You are a obesity level 1")
elif BMI2<39.9:
    print("You are a obesity level 2")
elif BMI2>30:
    print("You are severly obese go to a doctors ")

