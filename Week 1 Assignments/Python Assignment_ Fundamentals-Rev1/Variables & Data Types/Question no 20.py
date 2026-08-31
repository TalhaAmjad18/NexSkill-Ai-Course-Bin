# Swap the values of two variables a and b without using a third variable.

a = 1

b = 2

a = a + b 

b = a - b 

a = a - b

print(a, b)

# alternative

a = 1

b = 2

a, b = b, a

print(a, b)