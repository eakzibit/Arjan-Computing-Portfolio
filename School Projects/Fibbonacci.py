def fib(ui):   
 No1 = 0
 No2 = 1
 
 if ui < 0:
     print("Please enter a valid input")
 elif ui == 0:
     return 0
 elif ui == 1:
     return No2
 else:
     for i in range (1, ui):
         fib = No1 + No2
         No1 = No2
         No2 = fib
         print(fib)

fibNumber = int(input("How many times would you like to see the numbers ? "))

fib(fibNumber)
