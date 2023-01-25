d=int(input("enter the day:")) 
m=int(input("enter the month:"))
y=int(input("enter the year:"))
n=y-(14-m)/12
x=n+n/4-n/100+n/400
r=m+12*((14-m)/12)-2
z=(d+x+(31*r)/12)%7
i=int(z)
print(i) 
if(i==0):
 print("The day of the date is:Sunday") 
elif(i==1):
  print("The day of the date is:Monday") 
elif(i==2):
  print("The day of the date is:Tuesday") 
elif(i==3):
  print("The day of the date is:Wednesday")
elif(i==4):
   print("The day of the date is:Thursday")
elif(i==5):
   print("The day of the date is:Friday")
elif(i==6):
   print("The day of the date is:Saturday")
else:
   print("sorry")
   