# Python Program to Remove All Tuples in a List Outside the Given Range. The program removes 
# all tuples in a list of tuples with the USN outside the given range. 
# Problem Solution 
# 1. Take in the lower and upper roll number from the user. 
# 2. Then append the prefixes of the USN’s to the roll numbers. 
# 3. Using list comprehension, find out which USN’s lie in the given range. 
# 4. Print the list containing the tuples. 
# 5. Exit. 
# In the context of a university, a USN, or University Student Number, is a unique identifier 
# assigned to each student, acting as a primary identifier for their academic records and 
# interactions with the institution.

items = int(input("How many tuple items you want to add ? "))

outerList = []

innerList = []

for i in range(items):

    name = input("Enter name of student: ")

    innerList.append(name)

    rollNo = int(input("Enter roll no of student: "))
    
    innerList.append(rollNo)

    outerList.append(tuple(innerList))

    innerList.clear()

print(outerList)

lowerRange = int(input("Enter lower range of roll no: "))

upperRange = int(input("Enter upper range of roll no: "))

newStudentList = [i for i in outerList if i[1] >= lowerRange and i[1] <= upperRange]

print(newStudentList)