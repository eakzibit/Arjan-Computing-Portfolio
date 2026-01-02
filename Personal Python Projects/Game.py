x=input("what is your name?")
name=""

for i in range(0,len(x)):
    j=x[len(x)-1-i]
    name+=j    
print(name)
