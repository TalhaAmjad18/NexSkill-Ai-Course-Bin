# Python Program to Print All Permutations of a String in Lexicographic Order without Recursion. 
# The problem is the display all permutations of a string in lexicographic or dictionary order.

string = input("Enter a string: ")

sorted_string = sorted(string)

print(''.join(sorted_string))