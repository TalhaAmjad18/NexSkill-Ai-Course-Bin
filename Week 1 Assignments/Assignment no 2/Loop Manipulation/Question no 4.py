# Take Input from user , and print prime number till that input number 

num = int(input("Enter a number: "))

for i in range(2,num+1):

    count =0

    for j in range(1, num+1):

        if i % j ==0:

            count +=1

    if count == 2:

        print(f"{i} is a prime number")

    else:

        print(f"{i} is not a prime number")