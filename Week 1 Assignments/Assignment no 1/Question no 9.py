# Total Marks and Percentage 
# Input marks of 5 subjects. Print: 
# Total marks 
# Percentage 
# Average

marks_list = []
total_marks = 0
average = 0
percentage = 0

for i in range(5):
    marks = float(input(f"Enter marks of subject {i+1}: "))
    marks_list.append(marks)
    total_marks += marks_list[i]

print(f"Total marks: {total_marks}")

print(f"Average: {total_marks/len(marks_list)}")

print(f"Percentage: {(total_marks/500)*100}")