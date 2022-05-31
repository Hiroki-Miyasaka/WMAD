def checkNumbers(list, num):
    if num in list:
        print("ERROR:Number already exist in this list")
        return False
    else:
        return True

def InputList():
    number = int
    numbers = []
    while number != 0:
        number = int(input("Number:"))
        if checkNumbers(numbers, number):
          numbers.append(number)
    Sum = sum(numbers)
    print("Sum: ", Sum)

InputList()
