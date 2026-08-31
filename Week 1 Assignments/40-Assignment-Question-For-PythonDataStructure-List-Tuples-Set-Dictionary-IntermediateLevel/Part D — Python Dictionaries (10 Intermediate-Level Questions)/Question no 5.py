# 5. Filter a dictionary to keep only entries with values greater than 50.

marksDict = {
    'Ali': 45,
    'Sara': 78,
    'Ahmed': 52,
    'Ayesha': 30
}

updatedMarksDict = dict()

print(f"Marks dictionary: {marksDict}")

for key, value in marksDict.items():

    if value > 50:

        updatedMarksDict.update({key:value})

print(f"Filter a dictionary to keep only entries with values greater than 50: {updatedMarksDict}")