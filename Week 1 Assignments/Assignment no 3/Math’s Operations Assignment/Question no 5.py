# Python Program to Find the Sum of Natural Numbers. [Write a program that takes the number 
# of terms and calculates the sum of the first N natural numbers.]

n = int(input("Enter a number: "))

total = 0

for i in range(1, n+1):

    total += i

print(f"Sum of first {n} natural numbers is: {total}")