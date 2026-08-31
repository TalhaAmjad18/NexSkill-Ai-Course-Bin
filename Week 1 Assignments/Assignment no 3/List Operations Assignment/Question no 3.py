# Python Program to Print Largest Even and Largest Odd Number in a List. The program takes in a 
# list and prints the largest even and largest odd number in it. 

length = int(input("Enter length of list: "))

evenList = []

oddList = []

for i in range(length):

    elem = int(input(f"Enter element {i+1} in the list: "))

    evenList.append(elem) if elem % 2 == 0 else oddList.append(elem)

evenList.sort()

oddList.sort()

print(f"Largest even number is: {evenList[-1]}")

print(f"Largest odd number is: {oddList[-1]}")