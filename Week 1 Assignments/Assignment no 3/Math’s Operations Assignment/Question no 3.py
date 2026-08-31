# Python Program to Print an Identity Matrix [The program takes a number n and prints an 
# identity matrix of the desired size.]

n = int(input("Enter size of identity matrix: "))

for i in range(n):

    for j in range(n):

        if i == j:

            print(1,end=" ")
        
        else:

            print(0,end=" ")

    print()