# Python Program to Return the Length of the Longest Word from the List of Words. The program 
# takes a list of words and returns the word with the longest length.

length = int(input("Enter length of list: "))

l = []

d = dict()

for i in range(length):

    elem = input(f"Enter element {i+1} in the list: ")

    l.append(elem)

print(l)

for i in l:

    d.update({i:len(i)})

print(d)

x = 0

for key1 in d:

    x = d[key1]

    for key2 in d:

        if x < d[key2]:

            x = d[key2]

for key in d:

    if x == d[key]:

        print(f"Word with longest lenght is: {key}")