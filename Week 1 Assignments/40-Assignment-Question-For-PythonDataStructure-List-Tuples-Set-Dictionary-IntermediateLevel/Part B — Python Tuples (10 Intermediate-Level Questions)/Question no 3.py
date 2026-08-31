# 3. Write a function that returns multiple values (sum, min, max) using a tuple.

def function(numberList) -> tuple:

    total = sum(numberList)
    
    minimum = min(numberList)
    
    maximum = max(numberList)

    return total, minimum, maximum

numberList = [5, 10, 15, 20]

print(f"List of numbers: {numberList}")

total, minimum, maximum = function(numberList)

print(f"Sum of {numberList}: {total}")

print(f"Minimum value of {numberList}: {minimum}")

print(f"Maximum value of {numberList}: {maximum}")