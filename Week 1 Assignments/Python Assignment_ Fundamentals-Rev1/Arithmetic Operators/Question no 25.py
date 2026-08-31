#  Calculate the average of five numbers entered by the user. 

l = []

total = 0

for i in range(5):

    num = int(input(f"Enter number {i+1}: "))

    l.append(num)

    total += l[i]

print(f"Average of five numbers entered by user is {total / 5:.2f}")