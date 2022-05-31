
def showList9(num):
    myList9 = []
    while num > 0:
        if num % 9 == 0:
            myList9.append(num)
        num = num - 1
    print("9:", sorted(myList9))
def showList8(num):
    myList8 = []
    while num > 0:
        if num % 8 == 0:
            myList8.append(num)
        num = num - 1
    print("8:", sorted(myList8))
def showList7(num):
    myList7 = []
    while num > 0:
        if num % 7 == 0:
            myList7.append(num)
        num = num - 1
    print("7:", sorted(myList7))
def showList6(num):
    myList6 = []
    while num > 0:
        if num % 6 == 0:
            myList6.append(num)
        num = num - 1
    print("6:", sorted(myList6))
def showList5(num):
    myList5 = []
    while num > 0:
        if num % 5 == 0:
            myList5.append(num)
        num = num - 1
    print("5:", sorted(myList5))
def showList4(num):
    myList4 = []
    while num > 0:
        if num % 4 == 0:
            myList4.append(num)
        num = num - 1
    print("4:", sorted(myList4))
def showList3(num):
    myList3 = []
    while num > 0:
        if num % 3 == 0:
            myList3.append(num)
        num = num - 1
    print("3:", sorted(myList3))
def showList2(num):
    myList2 = []
    while num > 0:
        if num % 2 == 0:
            myList2.append(num)
        num = num - 1
    print("2:", sorted(myList2))
 
def inputNumber():
    num = int(input("Number:"))
 
    if num <= 50:
        print("ERROR: Need to be greater than 50")
    else:
        showList2(num)
        showList3(num)
        showList4(num)
        showList5(num)
        showList6(num)
        showList7(num)
        showList8(num)
        showList9(num)
 
inputNumber()
