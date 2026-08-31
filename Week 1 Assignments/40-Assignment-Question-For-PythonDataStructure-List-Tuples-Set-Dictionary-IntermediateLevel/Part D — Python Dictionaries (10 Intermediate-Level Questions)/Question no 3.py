# 3. Merge two dictionaries where second dictionary overrides first.

dictOneLength = int(input("Enter number of items you want to add in dictionary 1: "))

dictOne = dict()

for i in range(dictOneLength):

    key = input(f"Enter key of item {i+1} in dictionary 1: ")

    value = input(f"Enter value of item {i+1} in dictionary 1: ")

    dictOne.update({key:value})

print(f"Dictionary 1: {dictOne}")

dictTwoLength = int(input("Enter number of items you want to add in dictionary 2: "))

dictTwo = dict()

for i in range(dictTwoLength):

    key = input(f"Enter key of item {i+1} in dictionary 2: ")

    value = input(f"Enter value of item {i+1} in dictionary 2: ")

    dictTwo.update({key:value})

print(f"Dictionary 2: {dictTwo}")

dictThree = dict()

dictThree.update(dictOne)

dictThree.update(dictTwo)

print(f"Merge two dictionaries where second dictionary overrides first: {dictThree}")