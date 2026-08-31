# 4. Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list. 

t1 = (1, 2, 3)

t2 = (4, 5)

print(f"Tuple 1: {t1}")

print(f"Tuple 2: {t2}")

t3 = (t1 + t2)

print(f"Combining two tuples {t1} and {t2} : {t3}")

print(f"Convert {t3} to list : {list(t3)}")