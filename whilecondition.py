#program 1

i = 1
n = 5

while i <= n:
    print(i)
    i = i + 1

#program 2
t = 0

number = int(input('Enter a number: '))

while number != 0:
    t =t+ number
    number = int(input('Enter a number: '))

print('total =', t)


##program 4

counter = 0
while counter < 3:

    if counter == 2:
        break
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')



##program 6

i = 1

while i<=50:
    print(i)
    i = i + 1

#program 7

fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i+1




