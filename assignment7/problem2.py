

def enterWords():
    while words != "exit":
        list.append(words)
        words = input("enter English words")
    return list

words = input("enter English words\n")
tempList = []
print(enterWords())



# def organizeList(list):
#     myList = sorted(list)
#     print(myList)
#     return myList
 
# def inputList():
#     word = str
#     words = []
#     while word != "exit":
#         word = str(input("word:"))
#         if word != "exit":
#             words.append(word)
#     organizeList(words)
 
# inputList()