# Remove empty strings from the list of strings 

my_list = ["Python", "", "AI", "", "Machine Learning", "", "Data Science"]

updated_list = []

for i in range(len(my_list)):
    if my_list[i] == "":
        continue
    else:
        updated_list.append(my_list[i])

print(updated_list)