# Python Program to Check Armstrong Number 
# Armstrong Number in Python: Armstrong Number is an integer such that the sum of the cubes 
# of its digits is equal to the number itself. Armstrong numbers are 0, 1, 153, 370, 371, 407, etc. 
# Formula to calculate Armstrong Number: 
# wxyz = pow(w,n) + pow(x,n) + pow(y,n) + pow(z,n) 
# Example 1: 
# Let’s look at 153 as an example to understand why it’s an Armstrong number. 
# 153 = 1*1*1 + 5*5*5 + 3*3*3 
# = 1 + 125 + 27 
# = 153 
# Example 2: 
# Let’s look at 13 as an example to understand whether it’s an Armstrong number or not. 
# 13 = 1*1 + 3*3 
# = 1 + 9 
# = 10 
# Here, since 10 is not equal to 13, we can conclude that 13 is not an Armstrong number. 
# [Write a Python Program to check if a number is an Armstrong number. If the number is an 
# Armstrong then display “it is an Armstrong number” else display “it is not an Armstrong number”.]

num = int(input("Enter a number: "))

numString = str(num)

numList = []

cubeList = []

total = 0

for i in numString:

    numList.append(int(i))

for j in numList:

    cubeList.append(pow(j,len(numString)))

for k in cubeList:

    total += k

print(f"{num} is an Armstrong number") if total == num else print(f"{num} is not an Armstrong number")