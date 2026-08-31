#  Take Input from user , and print even number till that input number 

num = int(input("Enter a number: "))

for i in range(num+1):

    if i % 2 == 0:
    
        print(i)