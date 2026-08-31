# Sum of First N Natural Numbers 
# Input a number n, calculate sum of first n natural numbers. 
# Formula: sum = n * (n + 1) / 2

n = int(input("Enter a number: "))

sum1 = n * (n + 1) / 2

print(f"Sum of first {n} natural numbers is: {sum1}")

# Alternative method

sum2 = 0

for i in range(n+1):
    
    sum2 += i

print(f"Sum of first {n} natural numbers is: {sum2}")