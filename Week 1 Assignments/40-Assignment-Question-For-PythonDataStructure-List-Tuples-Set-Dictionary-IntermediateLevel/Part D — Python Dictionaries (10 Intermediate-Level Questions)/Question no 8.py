# 8. Find the key with the highest value in a dictionary.

marksDict = {
    'mahrukh': 80,
    'faakhir': 70,
    'sohail': 90
}

print(f"Marks dictionary: {marksDict}")

k = ""

v = 0

for key, value in marksDict.items():

    if value > v:

        v = value

        k = key

print(f"Key with the highest value in a dictionary is: {k}")