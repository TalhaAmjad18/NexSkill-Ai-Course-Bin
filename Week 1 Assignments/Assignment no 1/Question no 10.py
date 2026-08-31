# Salary Calculator 
# Input basic salary. Calculate: 
# HRA = 20% of basic 
# DA = 15% of basic 
# Total Salary = Basic + HRA + DA

basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20

print(f"HRA: {hra}")

da = basic_salary * 0.15

print(f"DA: {da}")

total_salary = basic_salary + hra + da

print(f"Total Salary: {total_salary}")