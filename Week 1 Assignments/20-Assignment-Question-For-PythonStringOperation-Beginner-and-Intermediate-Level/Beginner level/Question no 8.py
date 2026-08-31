# 8. Replace Substring
# Replace all occurrences of a word with another (case-sensitive).
# o Input: "I love apples. Apples are great!", "apples", "oranges"
# o Output: "I love oranges. Apples are great!"

string = input("Enter a string: ")

print(f"String is: {string}")

oldWord = input("Which word you want to replace? ")

newWord = input("With which word you want to replace? ")

print(f"After replacing {oldWord} with {newWord}, updated string is: {string.replace(oldWord,newWord)}")