# Distribute Items Equally - You have n candies and k students. 
# Write a program to find: 
# how many candies each student gets 
# how many are left

candies = float(input("Enter number of candies: "))

students = float(input("Enter number of students: "))

if candies < students:
    print("Candies can not be distributed equally")

elif (candies == students) or (candies % students == 0):
    x = candies / students
    print(f"Each student get {x} candies\nNo candies left")

else: 
    x = candies // students
    y = candies - (x * students)
    print(f"Each student get {x} candies\n{y} candies left")