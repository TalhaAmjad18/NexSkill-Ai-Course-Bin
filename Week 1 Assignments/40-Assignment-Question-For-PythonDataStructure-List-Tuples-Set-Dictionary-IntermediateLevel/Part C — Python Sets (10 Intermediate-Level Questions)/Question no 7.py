# 7. Count how many duplicate values exist in a list using sets.

numbersList = [1, 2, 2, 3, 4, 4, 4, 5]

print(f"List of numbers: {numbersList}")

numbersSet = set(numbersList)

print(f"Set of numbers: {numbersSet}")

d = {}

for i in numbersList:

    j = i

    counter = 0

    for k in numbersList:

        if j == k:

            counter += 1

    d.update({j:counter})

print(d)

counter = 0

for key, value in d.items():

    if value > 1:

        counter += 1

print(f"Number of duplicate values exist in list are: {counter}")