# Python Program to Remove Duplicates from a List. The program takes a lists and removes the 
# duplicate items from the list. 

length = int(input("Enter length of list: "))

l = []

for i in range(length):

    elem = int(input(f"Enter element {i+1} in the list: "))

    l.append(elem)

print(l)

s = set(l)

l = list(s)

print(f"After removing duplicates: {l}")