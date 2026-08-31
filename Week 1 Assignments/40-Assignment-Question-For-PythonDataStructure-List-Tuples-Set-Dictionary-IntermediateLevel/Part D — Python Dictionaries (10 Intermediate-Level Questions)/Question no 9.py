# 9. Combine two lists into a dictionary (keys from first list, values from second).

names = ['mahrukh', 'faakhir', 'sohail']

marks = [80, 89, 78]

print(f"List of names: {names}")

print(f"List of marks: {marks}")

studentDict = dict(zip(names,marks))

print(f"After combining two lists into a dictionary (keys from first list, values from second): {studentDict}")