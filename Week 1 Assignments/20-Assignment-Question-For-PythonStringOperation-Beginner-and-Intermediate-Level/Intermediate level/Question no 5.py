# 5. Character Frequency Dictionary
# Build a frequency dictionary for characters (case-insensitive, skip spaces).
# o Input: "Baa Baa Black Sheep"
# o Output (order may vary): {'b':3,'a':5,'l':1,'c':1,'k':1,'s':1,'h':1,'e':3,'p':1}

string = input("Enter a string: ")

updatedString = string.lower().replace(" ","")

countDict = dict()

print(updatedString)

for i in updatedString:

    j = i

    count = 0

    for k in updatedString:

        if j == k:

            count += 1

        else:

            continue

    countDict.update({j:count})

print(countDict)