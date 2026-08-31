# 4. Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension. 

twoDimensionalList = [[1, 2], [3, 4], [5]]

print(f"Original list: {twoDimensionalList}")

flattenList = [ j for i in twoDimensionalList for j in i ]

print(f"After flatten the nested list: {flattenList}")