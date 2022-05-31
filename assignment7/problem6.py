def combineListWithNoDublicate(list1,list2,list3):
  combineList = list(set(list1+list2+list3))
  print(str(combineList))


combineListWithNoDublicate([1,2,3],[2,3,4],[3,4,5])
