# Calculate Compound Interest 
# Use the formula: 
# CI = P * (1 + R/100)**T - P 
# Where P = principal, R = rate, T = time

principal_amount = float(input("Enter principal amount: ")) 

rate = float(input("Enter rate: "))

time = float(input("Enter time: "))

compound_interest = principal_amount * (1 + rate/100)**time - principal_amount

print(f"Compound Interest is: {compound_interest}")