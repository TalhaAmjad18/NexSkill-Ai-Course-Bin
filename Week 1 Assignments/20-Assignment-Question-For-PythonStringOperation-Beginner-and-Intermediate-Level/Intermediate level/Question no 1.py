# 1. Count Vowels & Consonants
# Count vowels and consonants (letters only; ignore digits/punctuation).
# o Input: "Hello, World! 123" -> Output: Vowels: 3, Consonants: 7

string = input("Enter a string: ")

countOne = countTwo = 0

for i in string.lower():

    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':

        countOne += 1

    elif i == 'b' or i == 'c' or i == 'd' or i == 'f' or i == 'g' or i == 'h' or i == 'j' or i == 'k' or i == 'l' or i == 'm' or i == 'n' or i == 'p' or i == 'q' or i == 'r' or i == 's' or i == 't' or i == 'v' or i == 'w' or i == 'x' or i == 'y' or i == 'z':

        countTwo += 1

print(f"String is : {string}")

print(f"Vowels in string are : {countOne}")

print(f"Consonants in string are : {countTwo}")