# 9. Split and Join
# Split a sentence on spaces and join with -.
# o Input: "split this sentence" -> Output: "split-this-sentence"

string = input("Enter a string: ")

print(f"String is: {string}")

splittedString = string.split()

hyphenatedString = "-".join(splittedString)

print(f"Hyphend string is: {hyphenatedString}")