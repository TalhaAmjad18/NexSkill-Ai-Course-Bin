# 1. Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements.

listSize = int(input("Enter size of list: "))

nums = []

for i in range(listSize):

    item = int(input(f"Enter item-{i+1} of the list: "))

    nums.append(item)

print(nums)

print(f"First element: {nums[0]}")

print(f"Last element: {nums[-1]}")