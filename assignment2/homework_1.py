import math

def calculater(x, y):
    return x*y + y*2 + abs(x - y)

num_x = input("input number x\n")
num_y = input("input number y\n")
numX = int(num_x)
numY = int(num_y)

print("1. answer is" + str(calculater(numX, numY)))

def calculater2(x, y):
    return 2*x + 3*y -5

print("2. answer is" + str(calculater2(numX, numY)))

