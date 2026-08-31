# 5. Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore 
# case. 

names = ['alice', 'Bob', 'charlie', 'DAVID']

print(f"Original list: {names}")

names.sort(key=str.lower)

print(f"Sorted alphabetically but ignoring case: {names}")