# Python Program to Count Number of Uppercase and Lowercase Letters in a String[The program 
# takes a string and counts the number of lowercase letters and uppercase letters in the string.]

string = input("Enter a string: ")

count_1 = 0 

count_2 = 0

for i in string:

    if i >= 'A' and i <= 'Z':

        count_1 += 1
    
    elif i >= 'a' and i <= 'z':

        count_2 += 1

    else:

        continue

print(f"Uppercase letters: {count_1} | Lowercase letters: {count_2}")