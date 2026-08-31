# 3. Count a Character
# Count how many times a given character appears in a string (case-sensitive).
# o Input: "banana", "a" -> Output: 3

string = input("Enter a string: ")

print(f"String is: {string}")

char = input("Enter character you want to count: ")

print(f"{char} is present {string.count(char)} times in {string}")