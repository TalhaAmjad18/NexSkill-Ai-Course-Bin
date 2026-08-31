# Replace list’s item with new value if found

my_list = ["Python", 2026, "AI", "Machine Learning", 3.14, True]

for i in range(len(my_list)):
    if my_list[i] == True:
        my_list[i] = False
    else:
        continue

print(my_list)