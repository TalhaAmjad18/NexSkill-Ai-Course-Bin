# 6. Slice a String
# Print a substring from index start to end (exclusive).
# o Input: "programming", 3, 8 -> Output: "gramm"

string = input("Enter a string: ")

print(f"String is: {string}")

start = int(input("Enter start index: "))

end = int(input("Enter end index: "))

stepSize = int(input("Enter start step size: "))

print(f"String after slicing: {string[start: end: stepSize]}")