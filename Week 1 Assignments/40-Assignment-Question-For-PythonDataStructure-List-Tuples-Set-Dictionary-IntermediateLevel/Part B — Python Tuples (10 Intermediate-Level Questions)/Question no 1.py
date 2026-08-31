# 1. Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables.

numbersList = [1, 2, 3, 4]

print(f"List of numbers: {numbersList}")

numbersTuple = tuple(numbersList)

print(f"Tuple of numbers: {numbersTuple}")

num1, num2, num3, num4 = numbersTuple

print(f"Number 1: {num1}")

print(f"Number 2: {num2}")

print(f"Number 3: {num3}")

print(f"Number 4: {num4}")