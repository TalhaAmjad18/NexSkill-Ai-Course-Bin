# Python Program to Swap the First and Last Element in a List. Python Program to Swap the First 
# and Last Element in a List

length = int(input("Enter length of list: "))

l = []

for i in range(length):

    elem = int(input(f"Enter element {i+1} in the list: "))

    l.append(elem)

print(l)

temp = l[0]

l[0] = l[-1]

l[-1] = temp

print(f"After swapping first and last element of list: {l}")