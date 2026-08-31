# Python Program to Create a New String Made up of First and Last 2 Characters. The program 
# takes a string and forms a new string made of the first 2 characters and last 2 characters from a 
# given string.

string = input("Enter a string: ")

new_string = string[0:2:1] + string[len(string)-2::1]

print(f"Given string: {string}\nNew string: {new_string}")