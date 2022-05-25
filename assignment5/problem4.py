# -	Design and implement a function which receives a number as its first input parameter and a format (which is either SHAPE1 or SHAPE2 or SHAPE3) as the second input parameter and prints the following patterns. See the examples below:

# -	Example: number: 5 format: SHAPE1
# *****
#  ***
#   *

# -	Example: number: 5 format: SHAPE2
# *****
# ****
# ***
# **
# *

# -	Example: number: 5 format: SHAPE3
# *
# **
# ***
# ****
# *****

#Problem2 Function
def shape_function(num, shape): 
  i = num
  a = "*"

  if(shape == "SHAPE3"):
    i = num + 2
    for i in range(1, i):
      for i in range(1, i):
        # print("*")
        print("%s" %a , end=""),
      print("") 
  elif(shape == "SHAPE2"):
    i = num + 1
    for i in range(i, 1, -1):
      for i in range(1, i):
        # print("*")
        print("%s" %a , end=""),
      print("") 
  elif(shape == "SHAPE1"):
    for i in range(num+1, 1, -1):
        for j in range(num - i):
            print(" ",end="")
        for k in range(1,i+1):
            print("*",end="")
        for m in range(1,i):
            print("*",end="")
        print()
    
  
num = int(input("Number:"))
shape = input("Please input shape: ")
shape_function(num,shape)