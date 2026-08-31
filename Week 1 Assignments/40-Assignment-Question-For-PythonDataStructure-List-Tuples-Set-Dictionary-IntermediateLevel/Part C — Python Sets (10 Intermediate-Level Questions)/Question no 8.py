# 8. Write a program to remove all vowels from a string using a set.

string = input("Enter a string: ")

stringList = []

vowelSet = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

for i in string:

    if i not in vowelSet:

        stringList.append(i)

updatedString = "".join(stringList)

print(f"Remove all vowels, string becomes: {updatedString}")