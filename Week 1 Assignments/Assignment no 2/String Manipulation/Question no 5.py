# Remove special symbols / punctuation from a string

string = input("Enter any string with special symbols / punctuation: ")

new_string = ""

for i in string:
    if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i >= str(0) and i <= str(9)):
        new_string += i

print(f"String without special symbols / punctuation: {new_string}")