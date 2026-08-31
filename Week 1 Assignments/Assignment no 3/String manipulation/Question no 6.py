# Python Program to Check if Two Strings are Anagram. [An anagram in Python is a pair of strings 
# that have the same characters, but in a different order. It involves rearranging the letters of one string to form the other.]

string_1 = input("Enter first string: ")

string_2 = input("Enter second string: ")

dictionary_1 = dict()

dictionary_2 = dict()

for i in string_1:

    j = i

    count = 0

    for k in string_1:

        if j == k:

            count += 1

    dictionary_1.update({j:count})

for i in string_2:

    j = i

    count = 0

    for k in string_2:

        if j == k:

            count += 1

    dictionary_2.update({j:count})

if dictionary_1 == dictionary_2:

    match = 0

    if len(string_1) != len(string_2):

        print("Strings are not anagram")

    else:

        for i in string_1:

            if i in string_2:

                match += 1

    if match == len(string_1):

        print("Strings are anagram")

    else:

        print("Strings are not anagram")    

else:

       print("Strings are not anagram")