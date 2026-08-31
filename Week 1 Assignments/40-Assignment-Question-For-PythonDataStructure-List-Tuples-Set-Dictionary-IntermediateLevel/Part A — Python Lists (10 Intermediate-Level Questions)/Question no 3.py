# 3. Remove duplicates from a list while preserving the original order. 

nums = [3, 1, 4, 1, 5, 9]

print(f"Original list: {nums}")

updatedList = []

for i in nums: 

    if i not in updatedList:

        updatedList.append(i)

print(f"After removing duplicates from a list while preserving the original order: {updatedList}")