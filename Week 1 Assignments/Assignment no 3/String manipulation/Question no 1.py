# Python Program to Check if a String is a Pangram or Not [The program takes a string and checks 
# if it is a pangram or not.]

string = input("Enter a string: ")

string_to_lower = string.lower()

if 'a' in string_to_lower and 'b' in string_to_lower and 'c' in string_to_lower and 'd' in string_to_lower and 'e' in string_to_lower and 'f' in string_to_lower and 'g' in string_to_lower and 'h' in string_to_lower and 'i' in string_to_lower and 'j' in string_to_lower and 'k' in string_to_lower and 'l' in string_to_lower and 'm' in string_to_lower and 'n' in string_to_lower and 'o' in string_to_lower and 'p' in string_to_lower and 'q' in string_to_lower and 'r' in string_to_lower and 's' in string_to_lower and 't' in string_to_lower and 'u' in string_to_lower and 'v' in string_to_lower and 'w' in string_to_lower and 'x' in string_to_lower and 'y' in string_to_lower and 'z' in string_to_lower:

    print("String is a Pangram")

else:

    print("String is not a Pangram")