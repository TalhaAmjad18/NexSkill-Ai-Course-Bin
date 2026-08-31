# 2. Palindrome Check (Ignore Case & Non-alphanumerics)
# Determine if a string is a palindrome ignoring case and non-alphanumeric characters.
# o Input: "A man, a plan, a canal: Panama!" -> Output: True

string = input("Enter a string: ")

print(f"String is: {string}")

stringLower = string.lower()

stringList = []

for i in stringLower:

    if i.isalnum():

        stringList.append(i)

    else:

        continue

updatedString = "".join(stringList)

if updatedString == updatedString[::-1]:

    print(True)

else:

    print(False)