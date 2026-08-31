# 2. Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements. 

t = (('a', 1), ('b', 2), ('c', 3))

print(f"Tuple of tuples: {t}")

l = []

for i in t:

    for j in range(len(i)):

        if j == 1:

            l.append(i[j])

print(f"After creating list of all second elements of tuple of tuples: {l}")