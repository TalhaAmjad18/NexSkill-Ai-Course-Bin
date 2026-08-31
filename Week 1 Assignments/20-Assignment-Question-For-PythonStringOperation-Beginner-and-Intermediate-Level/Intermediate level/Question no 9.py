# 9. Remove Duplicate Characters but Keep Order
# Remove duplicates while preserving the first occurrence order.
# o Input: "banana" -> Output: "ban"

string = input("Enter a string: ")

print(f"String is: {string}")

stringList = []

for i in string:

    if i not in stringList:

        stringList.append(i)

finalString = "".join(stringList)

print(f"After removing duplicates while preserving the first occurrence order: {finalString}")