# 2. Find common items between three sets using intersection. 

set1 = {1, 2, 3, 4, 18, 56}

set2 = {3, 4, 5, 6, 18, 56}

set3 = {5, 6, 7, 8, 18, 56}

print(f"Set 1: {set1}")

print(f"Set 2: {set2}")

print(f"Set 3: {set3}")

result = set1.intersection(set2.intersection(set3))

print(f"Common items between three sets using intersection: {result}")