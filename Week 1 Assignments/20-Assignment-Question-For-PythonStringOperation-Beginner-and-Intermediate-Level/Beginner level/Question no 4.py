# 4. First & Last Character
# Print the first and last character of a string; handle empty input.
# o Input: "drawer" -> Output: First: d, Last: r

string = input("Enter a string: ")

if len(string) == 0:

    print("Please enter a VALID string")

else:

    print(f"First character: {string[0]}")

    print(f"Last character: {string[-1]}")