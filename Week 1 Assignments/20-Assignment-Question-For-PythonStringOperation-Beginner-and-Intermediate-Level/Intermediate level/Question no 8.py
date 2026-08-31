# 8. Longest Word in a Sentence
# Find the longest word; if multiple, return the first. Consider words as alphabetic
# sequences.
# o Input: "Find the longest_word here!" -> Output: "longest

string = input("Enter a string: ")

stringList = []

for i in string:

    if i.isalpha() or i == " ":

        stringList.append(i)

    else:

        stringList.append(" ")

updatedString = "".join(stringList)

# print(updatedString)

updatedStringList = updatedString.split()

d = {}

for i in updatedStringList:

    count = len(i)

    d.update({i:count})

# print(d)

k = ""

val = 0

for key in d:

    if d[key] > val:

        val = d[key]

        k = key

print(f"Longest string is: {k}")