# Python Program to Find the Union of Two Lists. The program takes two lists and finds the unions 
# of the two lists.

length1 = int(input("Enter length of first list: "))

l1 = []

for i in range(length1):

    elem = int(input(f"Enter element {i+1} in the list 1: "))

    l1.append(elem)

print(l1)

length2 = int(input("Enter length of second list: "))

l2 = []

for i in range(length2):

    elem = int(input(f"Enter element {i+1} in the list 2: "))

    l2.append(elem)

print(l2)

set1 = set(l1)

set2 = set(l2)

result = set1.union(set2)

unionList = list(result)

print(f"Union of {l1} and {l2} is : {unionList}")