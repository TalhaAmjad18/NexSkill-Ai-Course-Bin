# Python Program to Calculate the Length of a String Without using Library Functions.[ The 
# program takes a string and calculates the length of the string without using library functions.

string = input("Enter a string: ")

count = 0

for i in string:

    count += 1

print(f"Length of {string} is: {count}")