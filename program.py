##multiplication
n=12
for i in range (0,11):
      print(n,"X",i,"=",n*i)


##with while

number  =int(input("Enter the table :"))
start   =int(input("Enter the starting number : "))
last   =int(input("Enter the limit :"))
while(start<=last):
  print(start,"*",number,"=",start * number)
  start=start+1

##program 3

l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)