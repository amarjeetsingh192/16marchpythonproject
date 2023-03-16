##program 1

def percent(marks):
    p = ((marks[0] + marks[1] + marks[2]+ marks[3])/400 )*100
    return p

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)
print(percentage1, percentage2)

##program

def greet(name="Stranger"):
    print("Good Day, " + name)


greet("Amarjeet")
greet()

##program 3

def farh(cel):
    return (cel *(9/5)) + 32

c = 0
f = farh(c)
print("Fahreheit Temperature is " + str(f))