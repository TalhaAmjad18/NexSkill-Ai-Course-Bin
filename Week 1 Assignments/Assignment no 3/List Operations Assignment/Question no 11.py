# Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List. The 
# program takes in the number of elements and generates random numbers from 1 to 20 and 
# appends them to the list.

import random

length = int(input("Enter length of list: "))

l = []

for i in range(length):

    l.append(random.randint(1,20))

print(l)