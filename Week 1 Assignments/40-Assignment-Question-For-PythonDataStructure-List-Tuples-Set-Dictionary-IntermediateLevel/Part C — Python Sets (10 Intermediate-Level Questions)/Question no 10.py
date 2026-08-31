# 10. Check if two strings are anagrams using set comparison (unique characters only).

stringOne = input("Enter string one: ")

stringTwo = input("Enter string two: ")

print(f"String 1: {stringOne}")

print(f"String 2: {stringTwo}")

setOne = set()

setTwo = set()

for i in stringOne:

    setOne.add(i)

for i in stringTwo:

    setTwo.add(i)

if setOne == setTwo:

    print(f"{stringOne} and {stringTwo} are anagram")

else:

    print(f"{stringOne} and {stringTwo} are not anagram")