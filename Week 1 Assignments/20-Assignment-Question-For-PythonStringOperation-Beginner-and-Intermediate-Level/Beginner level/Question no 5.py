# 5. Check Substring Presence
# Check if a substring exists in a string.
# o Input: "data science", "science" -> Output: True

string = input("Enter a string: ")

print(f"String is: {string}")

substring = input("Enter substring you want to check: ")

if substring in string:

    print(True)

else:

    print(False)