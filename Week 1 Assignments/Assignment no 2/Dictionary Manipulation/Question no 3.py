# Delete a list of keys from a dictionary

scores = {
    "Ali": 85,
    "Ahmed": 72,
    "Sara": 91,
    "Talha": 68,
    "Ayesha": 77,
    "Usman": 83
}

deleted_list = ["Ahmed", "Sara", "Amjad"]

for i in deleted_list:
    if i in scores.keys():
        del scores[i]
    else:
        print("Key not exist")

print(scores)