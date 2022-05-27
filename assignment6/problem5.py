def compareLists(list1, list2):
 
  a = set(list1)
  b = set(list2)
 
  if a == b:
      print("Lists l1 and l3 are equal")
  else:
      print("Lists l1 and l3 are not equal")
    
compareLists([1,2,3,4,5], [1,2,3,4,5])
compareLists([1,2,3,4,5], [6,7,8,9])
