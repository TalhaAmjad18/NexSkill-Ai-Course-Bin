# Python Program to Count Occurrences of Element in List. The program takes a number and 
# searches the number of times the particular number occurs in a list.

length = int(input("Enter length of list: "))

l = []

count = 0

for i in range(length):

    elem = int(input(f"Enter element {i+1} in the list: "))

    l.append(elem)

print(l)

num = int(input("Enter number you want to find in the list: "))

if num in l:

    for i in l:

        if i == num:

            count += 1

    print(f"{num} is present {count} times in the list")
        
else:

    print(f"{num} is not present in the list")