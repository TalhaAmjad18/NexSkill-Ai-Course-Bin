# Python Program to Create a List of Tuples with the First Element as the Number and Second 
# Element as the Square of the Number. The program takes a range and creates a list of tuples 
# within that range with the first element as the number and the second element as the square of 
# the number.

r = int(input("Enter range: "))

outerList = []

innerList = []

for i in range(r):

    x = i + 1

    innerList.append(x)
    
    innerList.append(x*x)

    outerList.append(tuple(innerList))

    innerList.clear()

print(outerList)