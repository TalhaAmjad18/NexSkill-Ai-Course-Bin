# 10. Store coordinates in tuples and calculate the Manhattan distance.

x1 = float(input("Enter x1 coordinate: "))

x2 = float(input("Enter x2 coordinate: "))

y1 = float(input("Enter y1 coordinate: "))

y2 = float(input("Enter y2 coordinate: "))

t1 = (x1, y1)

t2 = (x2, y2)

print(f"You enetered following coordinates; {t1} , {t2}")

dist = abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

print(f"Manhattan Distance between {t1} and {t2} : {dist}")