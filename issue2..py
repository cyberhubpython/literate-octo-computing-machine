revive = "y"
while revive == "y":
  f_num = float(input("Enter the first number:"))
  oper= input ("Enter the operation:")
  s_num = float(input("Enter the second number:"))
  if oper == '+' : 
    print (f_num + s_num)
  elif oper == "-":
   print(f_num - s_num)
  elif oper == "*":
   print(f_num * s_num)
  elif oper == "/":
   print(f_num / s_num)
  else :
   print("Error")
  revive = input("Enter 'y' to ontinue:")