# Python Program to Find Average of a List. The program takes the elements of the list one by one 
# and displays the average of the elements of the list.

length = int(input("Enter length of list: "))

total = 0

l = []

for i in range(length):

    elem = int(input(f"Enter element {i+1} in the list: "))

    l.append(elem)

print(l)

for i in l:

    total += i

print(f"Average of list elements is: {total/length}")