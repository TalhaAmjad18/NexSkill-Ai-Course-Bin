# Print multiplication table of a given number

num = int(input("Enter a number: "))

for i in range(1,11,1):
    
    print(f"{num} x {i} = {num * i}")