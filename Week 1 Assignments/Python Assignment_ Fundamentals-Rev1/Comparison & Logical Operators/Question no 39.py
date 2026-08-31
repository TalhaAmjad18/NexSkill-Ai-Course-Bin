#  Check if a number is positive and odd using logical operators. 

num = int(input("Enter a number: "))

if num >= 0 and num % 2 != 0:

    print(f"{num} number is positive and odd.")
    
else: 

    print(f"{num} number is not positive and odd.")