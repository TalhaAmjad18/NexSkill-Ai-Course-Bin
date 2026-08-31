# 4. Find All Indices of a Substring (Allow Overlaps)
# Return a list of starting indices where a substring occurs.
# o Input: s="aaaa", sub="aa" -> Output: [0, 1, 2]

stringList = []

string = input("Enter a string: ")

print(f"String is: {string}")

substring = input("Enter a substring: ")

print(f"Substring is: {substring}")

if substring not in string:

    print(f"{substring} is not present in {string}")

else:

    i = 0

    substringLength = len(substring)
    
    while i < len(string) - len(substring) + 1:
        
        item = string[i:substringLength+i:1]

        stringList.append(item)
        
        i+=1

countIndex = 0

indexArray = []

for i in stringList:

    if i == substring:

        indexArray.append(countIndex)
    
    countIndex += 1

print(indexArray)