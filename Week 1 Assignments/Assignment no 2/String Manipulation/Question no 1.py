# Write a program to create a new string made of an input string’s first, middle, and last character.

# for word string

character_list = []

string = input("Enter any string: ")

character_list.append(string[0])

character_list.append(string[(len(string)-1)//2])

character_list.append(string[len(string)-1])

new_string = "".join(character_list)

print(f"New string: {new_string}")