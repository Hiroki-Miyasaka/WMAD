#   Write a function which receives a list and returns True if the list is “Partially sorted” 
# and returns False if the list is not “Partially Sorted”. 
# A list is “Partially sorted” if and only if there exists an item in the list which if removed, 
# the list will become a sorted list. For instance the following list is “Partially sorted”:
# [1,2,5,10,6,8,9] This is partially sorted because it is not originally sorted 
# but if we remove 10 from the list, then the list is sorted. 

list1 = [1,5,10,6,8,9]

 
def isAscendedSort(list):
#   count = 1
#   size = len(list)
#   resp = False
#   for i in range(0, size):
    tmpList = []
      #　you are on the index i
      # you should try to remove item in the index i from the list can calculate the remaining item in the list
      # tmpList = [0..(i-1)] + [(i+1)...size]
      # you should check whether tmpList is a sorted list or not
      # if you find a tmpList which is sorted (ascending or descending) => return True
    for i in range(len(list)):
        temp = list[i]
        for j in range(i+1, len(list)):
            if temp > list[j]:
                for k in range(0, i):
                    tmpList.append(list[k])
                for l in range(i+1, len(list)):
                    tmpList.append(list[l])
            #print(list)
                

    return tmpList


def AscendOrNot(list):
    newList = sorted(list)
    print(list)
    print(newList)
    if list == newList:
        return True
    return False

def main(list):
    listLength = len(list)
    if len(isAscendedSort(list)) == listLength:
        # print(len(isAscendedSort(list)))
        # print(len(list))
        return False
    return AscendOrNot(isAscendedSort(list))

print(main(list1))

#再帰
list1 = [1,2,11,5,10,8,9]

def isAscendedSort(list):
    return isAscendedSortHelper(list, 0, 0)

def isAscendedSortHelper(list, index, count):
    listLength = len(list)
    #print(count)
    if count >= 1 or index >= listLength - 1:
        print("ok")
        return list
       
    if list[index] > list[index+1]:
        list.pop(index)
        return isAscendedSortHelper(list, index+1, count+1)
    return isAscendedSortHelper(list, index+1, count)


def AscendOrNot(list):
    newList = sorted(list)
    print(list)
    print(newList)
    if list == newList:
        return True
    return False

def main(list):
    listLength = len(list)
    if len(isAscendedSort(list)) == listLength:
        # print(len(isAscendedSort(list)))
        # print(len(list))
        return False
    return AscendOrNot(isAscendedSort(list))


print(main(list1))
