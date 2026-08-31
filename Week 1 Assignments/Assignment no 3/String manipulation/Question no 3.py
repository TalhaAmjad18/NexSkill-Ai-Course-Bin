# This is a Python Program to display which letters are in the two strings but not in both.

string_1 = input("Enter first string: ")

string_2 = input("Enter second string: ")

for i in string_1:

    if i in string_2:

        continue

    else:

        print(i)


for i in string_2:

    if i in string_1:

        continue

    else:

        print(i)