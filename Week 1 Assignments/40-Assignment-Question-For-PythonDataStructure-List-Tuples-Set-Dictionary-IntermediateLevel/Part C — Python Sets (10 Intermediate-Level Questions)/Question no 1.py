# 1. Given two sets, find elements that are in the first set but not the second.

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

print(f"Set 1: {set1}")

print(f"Set 2: {set2}")

print(f"Elements in first set but not second set: {set1.difference(set2)}")