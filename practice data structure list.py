bookList = [445, "Think and Grow Rich", "Napoleon Hill", 50.5]

print(bookList)

print(type(bookList))

print(len(bookList))

for i in bookList:

    print(i)

print(bookList[2])

print(type(bookList[2]))

print(type(bookList[3]))

bookList.append("ABC Publisher")

print(bookList)

bookList.insert(1, 1937)

print(bookList)

bookList.remove(50.5)

print(bookList)