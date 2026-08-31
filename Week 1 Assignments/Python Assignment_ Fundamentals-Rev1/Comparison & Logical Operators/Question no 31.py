# Compare two numbers entered by the user and print if the first is greater than the 
# second.

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

if num1 > num2:

    print(f"{num1} is greater than {num2}")

elif num1 < num2:

    print(f"{num1} is less than {num2}")

else:

    print(f"{num1} and {num2} are equal")