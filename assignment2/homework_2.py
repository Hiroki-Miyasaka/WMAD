import math

def calculater(w, x, y, z):
    return max(w, x, y, z) - min(w, x, y, z) + w*x + abs(y - z)

X1 = input("enterX1\n")
X2 = input("enterX2\n")
X3 = input("enterX3\n")
X4 = input("enterX4\n")

x1 = int(X1)
x2 = int(X2)
x3 = int(X3)
x4 = int(X4)

print("answer is " + str(calculater(x1, x2, x3, x4)))
