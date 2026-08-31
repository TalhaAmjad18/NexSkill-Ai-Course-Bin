# 7. Write a dictionary comprehension that maps numbers 1–10 to their cubes.

cubeDict = {
    i: pow(i,3)
    for i in range(1,11)
}

print(f"Dictionary comprehension that maps numbers 1–10 to their cubes: {cubeDict}")