def haveWord():
  word = "   "
  i = 0
  list = []
  while word != "":
    word = str(input("Word:"))
    if (word in list):
      print("ALREADY EXISTs")
    else:
      i = i + 1
      list.insert(i, word)
      print("DONT EXISTs")

haveWord()


# list = []

# def addListbyInput(word):
#   count = 0
#   while (len(word)):
#     if len(list) !=0:
#       for i in range(len(list)):
#         if word == list[i]:
#           count = count + 1
#           print ("This word has already inputed...")

#       if count == 0:
#         list.append(word)
#     else:
#       list.append(word)
#     word = input("Let's input your favorite word : ")
  
#   print('You inputed these word. %s' %list)
      

# addListbyInput(input("Let's input your favorite word : "))
