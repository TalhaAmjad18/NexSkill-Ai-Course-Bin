# Python Program to Check If Two Numbers are Amicable Numbers or Not[The program takes two 
# numbers and checks if they are amicable numbers.] Amicable numbers are pairs of different 
# numbers where the sum of the proper divisors (divisors excluding the number itself) of one 
# number equals the other number, and vice versa. The smallest example is 220 and 284. 

num_1 = int(input("Enter first number: "))

num_2 = int(input("Enter second number: "))

list_1 = []

list_2 = []

for i in range(1, num_1+1):

    if num_1 % i == 0:

        list_1.append(i)

for i in range(1, num_2+1):

    if num_2 % i == 0:

        list_2.append(i)

list_1.remove(num_1)

list_2.remove(num_2)

if num_1 == sum(list_2) and sum(list_1) == num_2:

    print(f"{num_1} and {num_2} are Amicable Numbers")

else:

    print(f"{num_1} and {num_2} are not Amicable Numbers")