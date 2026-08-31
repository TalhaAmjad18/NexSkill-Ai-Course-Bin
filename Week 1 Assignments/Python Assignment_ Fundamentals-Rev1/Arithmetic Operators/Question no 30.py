# Write a program to calculate simple interest: (P \times R \times T) / 100.

p = float(input("Enter principal amount: "))

r = float(input("Enter rate of interest: "))

t = float(input("Enter number of years: ")) 

simpleInterest = (p * r * t) / 100

print(f"Simple interest with principal amount of Rs.{p}, rate of interest {r} and number of years {t} is {simpleInterest}")