import  random


question = "A for loop is an example of a...?"
options = ["count-controlled loop","condition-controlled loop",
           "counter-culture loop","remote-controlled loop"]

ca="count-controlled loop"
random.shuffle(options)

print(question)
print("1)",options[0])
print("2)",options[1])
print("3)",options[2])
print("4)",options[3])

while options!=ca:
  choice = int(input("Awnser 1-4: "))
  if options[choice-1]== ca:
    print("right!")
    break
  else:
    print("wrrrrrrrrrrrong")

      
