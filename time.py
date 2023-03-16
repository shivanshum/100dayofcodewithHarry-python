import time 
timestamp = time.strftime('%H:%M:%S:%P:%Z')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# hour = int(input("Enter time in 24 hrs"))
hour = int(time.strftime('%H'))
if(hour >= 4 and  hour <= 12):
  print("Good Morning Sir!")
elif(hour >12 and hour <=18):
  print("Good Afternoon Sir!")
else:
  print("Good Night Sir!")