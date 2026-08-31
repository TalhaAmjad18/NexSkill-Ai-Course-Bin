# 10. Remove all keys from a dictionary whose values are None.

marksDict = {
    'mahrukh': 80,
    'faakhir': 70,
    'sohail': 90,
    'ayesha': None,
    'ali': 70,
    'sadaf': None,
}

print(f"Marks dictionary: {marksDict}")

updatedMarksDict = dict()

for key, value in marksDict.items():

    if value is not None:

        updatedMarksDict.update({key:value})

print(f"After removing all keys from a dictionary whose values are None: {updatedMarksDict}")