# 5. Check if one set is a strict subset of another.

set1 = {1, 2}

set2 = {1, 2, 3, 4}

print(f"Set 1: {set1}")

print(f"Set 2: {set2}")

if len(set1) < len(set2) and set1.issubset(set2):

    print(f"{set1} is strict subset of {set2}")

else:

    print(f"{set1} is not strict subset of {set2}")