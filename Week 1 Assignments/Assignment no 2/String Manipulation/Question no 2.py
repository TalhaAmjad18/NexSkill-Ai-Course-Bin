# Write a program to count occurrences of all characters within a string

string = input("Enter any string: ")

count = 0

count_dict = {}

for i in string:
    count = 0
    j = i
    for k in string: 
        if j == k:
            count+=1
    count_dict.update({j:count})

print(count_dict)