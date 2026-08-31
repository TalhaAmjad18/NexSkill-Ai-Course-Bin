# 10. Create a dictionary from two lists: keys = ['a','b'], values = [1,2].

keys = ['a', 'b']

values = [1, 2]

a, b = keys

x, y = values

d1 = {
    a: x,
    b: y
}

print(f"Keys: {keys}\nValues: {values}\nDictionary:{d1}")

# alternate way

d2 = dict(zip(keys, values))

print(f"Keys: {keys}\nValues: {values}\nDictionary:{d2}")