# 6. Anagram Checker
# Check if two strings are anagrams (ignore spaces, punctuation, and case).
# o Input: "Listen", "Silent" -> Output: True

stringOne = input("Enter string one: ").lower().replace(" ","")

stringTwo = input("Enter string two: ").lower().replace(" ","")

listOne = []

listTwo = []

for i in stringOne:

    if i.isalnum():

        listOne.append(i)

for i in stringTwo:

    if i.isalnum():

        listTwo.append(i)

updatedStringOne = "".join(listOne)

updatedStringTwo = "".join(listTwo)

print(updatedStringOne,updatedStringTwo)

countDictOne = dict()

for i in updatedStringOne:

    j = i

    count = 0

    for k in updatedStringOne:

        if j == k:

            count += 1

        else:

            continue

    countDictOne.update({j:count})

print(countDictOne)

countDictTwo = dict()

for i in updatedStringTwo:

    j = i

    count = 0

    for k in updatedStringTwo:

        if j == k:

            count += 1

        else:

            continue

    countDictTwo.update({j:count})

print(countDictTwo)

if countDictOne == countDictTwo:

    print(True)

else:

    print(False)