# Reverse the tuple 

my_tuple = ("Python", 2026, "AI", "Machine Learning", 3.14, True)

new_tuple = ()

for i in range(len(my_tuple)-1,-1,-1):
    new_tuple = new_tuple + (my_tuple[i],)

print(new_tuple)

# Alternative way 

t = my_tuple[::-1]

print(t)