# 8. Create a new list containing only elements that appear exactly once in the original 
# list.

numbers = [4, 7, 12, 7, 9, 15, 7, 21, 5, 7, 18, 7]

print(f"List of numbers: {numbers}")

updatedList = []

for i in numbers:

    if numbers.count(i) == 1:

        updatedList.append(i)

print(f"New list containing only elements that appear exactly once in the original list: {updatedList}")