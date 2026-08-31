# Compare the lengths of two strings provided by the user.

stringOne = input("Enter string one: ")

stringTwo = input("Enter string two: ")

if len(stringOne) == len(stringTwo):

    print(f"Length of {stringOne} = Length of {stringTwo}")

elif len(stringOne) < len(stringTwo):

    print(f"Length of {stringOne} < Length of {stringTwo}")

elif len(stringOne) > len(stringTwo):

    print(f"Length of {stringOne} > Length of {stringTwo}")

else:

    print()