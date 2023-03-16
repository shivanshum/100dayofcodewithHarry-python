a = int(input("Enter Your Age"))
print("Your Age is:", a)
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>18):
  print("you can drive")
else:
  print("you can't drive")
#nested if else
appleprice = 10
budget = 200
if(budget - appleprice >50):
  print("Add 1 kg of apples to the cart")
elif(budget - appleprice >70):
  print("Its ok you can buy")
else:
  print("Don't add apples to the cart")