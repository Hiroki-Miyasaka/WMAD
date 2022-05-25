#Design and implement a function with one parameter which is an integer and finds the 
#next prime number which is bigger than the given input parameter and returns it.
#Reuse (call) the function you have defined for Problem 2

def prime_function(num):  
  response = False

  biggerNumber = num +1
  
  if biggerNumber > 1:
    while response != True:
      for i in range(2, biggerNumber):
          if (biggerNumber % i) == 0:
            response = True
            break
      biggerNumber = biggerNumber +1
          
  print(biggerNumber)

  
num = int(input("Number:"))
prime_function(num)
