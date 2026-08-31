# Python Program to Multiply All the Items in a Dictionary. The program takes a dictionary and 
# prints the product of all the items in the dictionary.  

d = dict()

length = int(input("How many items you want to add in dictionary? "))

for i in range(length):

    key = input(f"Enter key of item {i+1}: ")
    
    value = int(input(f"Enter value of item {i+1}: "))

    d.update({key:value})

print(d)

total = 1

for key in d:

    total *= d[key]

print(f"Total product of items: {total}")