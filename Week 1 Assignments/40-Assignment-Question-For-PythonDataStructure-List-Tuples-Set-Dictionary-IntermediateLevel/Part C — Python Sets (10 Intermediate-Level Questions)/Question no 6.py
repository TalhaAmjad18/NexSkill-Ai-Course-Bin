# 6. Use a set comprehension to collect all squares of numbers from 1–15 that are 
# divisible by 3. 

s = set([ pow(i,2) for i in range(1,16) if pow(i,2) % 3 == 0 ])

print(f"All sqaures of numbers from 1-15 that are divisible by 3: {s}")