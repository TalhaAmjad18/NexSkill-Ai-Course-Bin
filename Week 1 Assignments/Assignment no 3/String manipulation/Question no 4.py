# Python Program to Find the Larger String without using Built-in Functions[The program takes in 
# two strings and display the larger string without using built-in function.] 

string_1 = input("Enter first string: ")

string_2 = input("Enter second string: ")

count_1 = 0

count_2 = 0

for i in string_1.strip():

    count_1 += 1

for i in string_2.strip():

    count_2 += 1

if count_1 > count_2:

    print(f'Length: {count_1} \n {string_1}')

elif count_1 < count_2:

    print(f'Length: {count_2} \n {string_2}')

else:

    print(f'Length: {count_1} \n {string_1} \n {string_2}')    