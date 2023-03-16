##program break
counter = 0
while counter < 3:

    if counter == 2:
        break
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')


##program pass

counter = 0
while counter < 3:

    if counter == 1:
        pass
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

##program cont

counter = 0
while counter < 3:

    if counter == 3:
        continue
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')
## program break2

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for")

