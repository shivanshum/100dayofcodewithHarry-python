num = int(input("Enter a number"))
if(num < 0):
  print("Number is Negative")
elif(num >0):
  if(num <=10):
    print("Number is Between 1-10")
  elif(num >10 and num <=20):
    print("Number is Betweeen 11-20")
  else:
    print("Number is Greater than 20")
else:
  print("Number is Zero")