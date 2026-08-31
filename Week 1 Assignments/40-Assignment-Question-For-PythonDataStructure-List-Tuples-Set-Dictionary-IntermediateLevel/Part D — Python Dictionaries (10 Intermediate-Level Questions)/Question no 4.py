# 4. Group words by their first letter into a dictionary of lists. 

string = input("Enter a string: ")

print(f"String: {string}")

splittedString = string.split()

d = dict()

for i in splittedString:

    j = i[0]

    l = []

    for k in splittedString:

        if j == k[0]:

            l.append(k)

    d.update({j:l})

print(d)