list = []

numbersInput = int(input("Digit how many numbers: "))


def listInput(num):
  i = 0
  while i != num:
    i = i + 1
    number = int(input("Number: "))
    list.append(number)
  print(list)

