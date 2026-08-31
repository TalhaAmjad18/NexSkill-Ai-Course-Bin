# 7. Create a set {'a', 'b'} and add 'c' only if it's missing.

s = {'a', 'b'}

print(f"Set: {s}")

if 'c' not in s:

    s.add('c')

    print(f"After adding c, Set becomes: {s}")

else:

    print(f"c is already present in {s}")