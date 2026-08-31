# Python Program to Find the Number Occurring Odd Number of Times in a List. A list is given in 
# which all elements except one element occurs an even number of times. The problem is to find 
# the element that occurs an odd number of times. 

length = int(input("Enter length of list: "))

l = []

d = dict()

count = 0

for i in range(length):

    elem = int(input(f"Enter element {i+1} in the list: "))

    l.append(elem)

print(l)

for i in l:

    j = i

    for k in l:

        if j == k:

            count += 1

    d.update({j:count})

    count = 0

for key in d:

    if d[key] % 2 != 0:

        print(f"{key} occured odd times")