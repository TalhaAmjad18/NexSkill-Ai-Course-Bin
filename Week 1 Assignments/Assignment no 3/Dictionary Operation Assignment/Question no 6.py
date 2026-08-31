# Python Program to Concatenate Two Dictionaries. The program takes two dictionaries and 
# concatenates them into one dictionary.

d1 = dict()

length1 = int(input("How many items you want to add in dictionary 1 ? "))

for i in range(length1):

    key = input(f"Enter key of item {i+1}: ")
    
    value = int(input(f"Enter value of item {i+1}: "))

    d1.update({key:value})

print(d1)

d2 = dict()

length2 = int(input("How many items you want to add in dictionary 2 ? "))

for i in range(length2):

    key = input(f"Enter key of item {i+1}: ")
    
    value = int(input(f"Enter value of item {i+1}: "))

    d2.update({key:value})

print(d2)

d3 = dict()

d3.update(d1)

d3.update(d2)

print(f"Concatenated dictionary: {d3}")