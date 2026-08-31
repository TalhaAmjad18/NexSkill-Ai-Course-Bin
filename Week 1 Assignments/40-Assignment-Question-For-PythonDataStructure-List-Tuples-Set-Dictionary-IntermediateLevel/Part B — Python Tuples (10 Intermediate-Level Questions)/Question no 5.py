# 5. Given a tuple of numbers, find the element with the highest frequency.

numbers = (2, 5, 2, 8, 2, 3, 5)

print(f"Tuple: {numbers}")

d = {}

for i in numbers:

    j = i

    counter = 0

    for k in numbers:

        if j == k:

            counter += 1

    d.update({i:counter})

k = ""

v = 0

for key, value in d.items():

    if value > v:

        v = value

        k = key

print(f"Element with highest frequency is: {k}") 