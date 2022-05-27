def common_elements():
  i = 0
  function = str(input("Function"))
  value = 0
  if(len(function) > 10):
    print("Cant have more than 10 digits")
  else:
    for i in range(0, len(function)):
      if(function[i] == "*"):
        value += int(function[i-1]) * int(function[i+1])
      elif(function[i] == "^"):
        value += int(function[i-1]) ** int(function[i+1])
      elif(function[i] == "-"):
        value += int(function[i-1]) - int(function[i+1])
      elif(function[i] == "+"):
        value += int(function[i-1]) + int(function[i+1])
      elif(function[i] == "/"):
        value += int(function[i-1]) / int(function[i+1])

  return value

print(common_elements())
