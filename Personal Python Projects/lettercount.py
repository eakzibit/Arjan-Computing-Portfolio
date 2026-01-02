#print("DO NOT ENTER ANY SPACES AND CAPITALS WRITE IT AS ONE WORD")
#word=input("what is your word? ")
#letter=input("what is the letter you want ")
#sentence=word.count(letter)
#averageone=sentence/len(word)
#average=averageone*100
#print(average)



word = input("please type a word with no spaces: ")
letter = input("please letter to count: ")
count=0

for i in range(0,len(word)):
    if word[i].islower() and word[i]==letter:
        count+=1

print(count)
print(count/len(word))
