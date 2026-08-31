# 9. Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4).

nestedTuple = ((1,2),(3,4))

print(f"Nested tuple: {nestedTuple}")

flattenTuple = ()

for i in nestedTuple:

    for j in i:

        flattenTuple = flattenTuple + (j,)

print(f"Flatten tuple: {flattenTuple}")