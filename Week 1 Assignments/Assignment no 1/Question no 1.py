# Write a program that converts a temperature from Celsius to Fahrenheit. 
# (Formula: Fahrenheit = (Celsius * 9/5) + 32)

celsius = float(input("Enter temperature in celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} C temperature is equal to {fahrenheit} F")