# Python Program to Find All Perfect Squares in the Given Range.[ The program takes a range and 
# creates a list of all numbers in the range which are perfect squares and the total of the digits is 
# less than 10.] To find perfect squares within a range, identify the smallest and largest integers 
# whose squares fall within that range, then list the squares of those integers.  
# Example: 
# Range: 1 to 100 
# Smallest integer: 1 (1 * 1 = 1) 
# Largest integer: 10 (10 * 10 = 100) 
# Perfect Squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

import math

startRange = int(input("Enter start of range: "))

endRange = int(input("Enter end of range: "))

squaredList = []

loopLowerLimit = math.ceil(math.sqrt(startRange))

loopUpperLimit = math.floor(math.sqrt(endRange))

for i in range(loopLowerLimit, loopUpperLimit+1):

    result = i * i

    squaredList.append( str(result) )

print(squaredList)

checkList = []

updatedSquaredList = []

for i in squaredList: 

    for j in i: # j =1

        checkList.append(int(j))

    total = 0

    for l in checkList:

        total += l

    if total < 10:

        updatedSquaredList.append(i)
    
    checkList.clear()

print(updatedSquaredList)