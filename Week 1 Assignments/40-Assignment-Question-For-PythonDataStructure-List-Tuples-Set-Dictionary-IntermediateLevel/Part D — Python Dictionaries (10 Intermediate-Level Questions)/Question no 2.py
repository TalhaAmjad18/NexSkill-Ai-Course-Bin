# 2. Invert a dictionary where all values are unique.

itemsLength = int(input("Enter number of items you want to add in dictionary: "))

d = dict()

for i in range(itemsLength):

    key = input(f"Enter key of item {i+1}: ")

    value = input(f"Enter value of item {i+1}: ")

    d.update({key:value})

print(f"Original dictionary: {d}")

updatedDict = dict()

for key, value in d.items():

    updatedDict.update({value:key})

print(f"Inverted dictionary: {updatedDict}")