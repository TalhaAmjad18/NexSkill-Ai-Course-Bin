# 1. Create a list comprehension that returns the squares of only the even numbers from 
# 0–20.

evenSquaredList = [ i * i for i in range(0, 21) if i % 2 == 0 ]

print(f"List of squares of even numbers from 0-20: {evenSquaredList}")