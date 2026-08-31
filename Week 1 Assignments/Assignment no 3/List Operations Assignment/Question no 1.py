# This is a Python Program to find the largest number in a list. The program takes a list and prints 
# the largest number in the list.

length = int(input("Enter length of list: "))

l = []

for i in range(length):

    elem = int(input(f"Enter element {i+1} in the list: "))

    l.append(elem)

print(l)

l.sort()

print(f"Largest number in list is: {l[length-1]}")