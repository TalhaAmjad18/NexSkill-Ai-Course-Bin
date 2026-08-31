# Python Program to Create Dictionary that Contains Number. The program takes a number from 
# the user and generates a dictionary that contains numbers (between 1 and n) in the form 
# (x,x*x).

length = int(input("Enter number of items: "))

d = dict()

for i in range(length):

    x = i + 1

    d.update({x:x*x})

print(d)