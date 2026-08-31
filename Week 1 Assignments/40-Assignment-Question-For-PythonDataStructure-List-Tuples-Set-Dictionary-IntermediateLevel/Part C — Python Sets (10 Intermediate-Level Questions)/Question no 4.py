# 4. Convert a list with duplicates into a set, then back to a sorted list.

numbersList = [4, 2, 7, 2, 9, 4, 1]

print(f"List of numbers: {numbersList}")

numbersSet = set(numbersList)

print(f"Set of numbers: {numbersSet}")

uniqueNumbersList = list(numbersSet)

uniqueNumbersList.sort()

print(f"Sorted list of unique numbers: {uniqueNumbersList}")