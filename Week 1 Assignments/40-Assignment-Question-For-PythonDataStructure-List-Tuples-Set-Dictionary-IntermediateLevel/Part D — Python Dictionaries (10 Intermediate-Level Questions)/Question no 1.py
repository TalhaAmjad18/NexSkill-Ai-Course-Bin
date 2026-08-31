# 1. Count word frequencies in a sentence and store the results in a dictionary. 

string = input("Enter a string: ")

splittedString = string.split()

d = {}

for i in splittedString:

    j = i

    counter = 0

    for k in splittedString:

        if j == k:

            counter += 1

    d.update({j:counter})

print(d)