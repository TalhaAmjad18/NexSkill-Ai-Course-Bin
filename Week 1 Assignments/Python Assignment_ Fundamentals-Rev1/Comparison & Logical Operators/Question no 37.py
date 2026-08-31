# Compare two floating-point numbers: 0.1 + 0.2 == 0.3. Explain the result. 

a, b, c = 0.1, 0.2, 0.3

if a + b == c:

    print(f"{a} + {b} == {c}")

else:
    
    print(f"{a} + {b} != {c}")

# output will be: 0.1 + 0.2 != 0.3 because 0.1 + 0.2 results in 0.300000... not 0.3