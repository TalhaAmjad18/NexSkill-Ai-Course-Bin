# 7. Write a program to find all indices of a value in a list (e.g., all indices of 7).

numbers = [4, 7, 12, 7, 9, 15, 7, 21, 5, 7, 18, 7]

print(f"List of numbers: {numbers}")

counter = 0

counterList = []

for i in numbers:

    if i == 7:

        counterList.append(counter)

    counter += 1

print(f"All indices of value 7 in list are: {counterList}")