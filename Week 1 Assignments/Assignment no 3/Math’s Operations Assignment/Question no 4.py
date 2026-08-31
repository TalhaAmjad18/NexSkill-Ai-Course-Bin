# Python Program to Find the LCM of Two Numbers [The program takes two numbers and prints 
# the LCM of two numbers.]

num_1 = int(input("Enter first number: "))

num_2 = int(input("Enter second number: "))

list_1 = []

list_2 = []

for i in range(1, num_1+1):

    if num_1 % i == 0:

        list_1.append(i)

for i in range(1, num_2+1):

    if num_2 % i == 0:

        list_2.append(i)

print(f"Factors of {num_1}: {list_1}")

print(f"Factors of {num_2}: {list_2}")

set_1 = set(list_1)

set_2 = set(list_2)

gcd = max(set_1.intersection(set_2))

print(f"GCD: {gcd}")

lcm = (num_1 * num_2) // gcd

print(f"LCM of {num_1} and {num_2}: {lcm}")