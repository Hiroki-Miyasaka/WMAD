

list1 = [1,2,11,5,10,8,9]

def isAscendedSort(list):
    tmpList = []
    return isAscendedSortHelper(list, 0, tmpList)

def isAscendedSortHelper(list, index, tmpList):
    listLength = len(list)
    #print(count)
    if list[index] > list[index+1] or index >= listLength - 1:
        #print("ok")
        for i in range(index+1, len(list)):
            tmpList.append(list[i])
        return tmpList
    return isAscendedSortHelper(list, index+1, tmpList.append(list[index]))


def AscendOrNot(list):
    newList = sorted(list)
    rNewList = sorted(list, reverse=True)
    print(list)
    print(newList)
    if list == newList or list == rNewList:
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
