x = int(input("Enter the value "))
match x:
    case 0:
      print("X is Zero")
    case 4:
      print("Case is 4")
    case _ if x!=80 :
      print(x,"x is not 80")
    case _ if x!=90:
      print(x,"x is not 90")