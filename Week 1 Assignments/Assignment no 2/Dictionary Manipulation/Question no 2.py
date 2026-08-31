# Get the key of a minimum value from the following dictionary 

scores = {
    "Ali": 85,
    "Ahmed": 72,
    "Sara": 91,
    "Talha": 68,
    "Ayesha": 77,
    "Usman": 83
}

min_val = 100

for key, value in scores.items():
    if scores[key] < min_val:
        min_val = scores[key]

for key, value in scores.items():
    if scores[key] == min_val:
        print(key)
        break