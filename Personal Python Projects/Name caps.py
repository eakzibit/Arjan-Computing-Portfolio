name=input("what is your name? ")
reverseName = ""
      
for i in range(0, len(name)):
    j=len(name)-1-i
    reverseName += name[j]

print("Your name in reverse is " + reverseName)

array = [1,2,3,4,10]
sum = 0
for i in range(0, len(array)):
    sum += array[i]

print(array)
array.sort(key=None,reverse=True)
print(array)
print("Here are some interesting stats about the array: ")
print("There are "  + str(len(array)) + " numbers in the array")
print("The sum of the array is: " + str(sum))
print("The average of the array is: " + str(sum/len(array)))





           
