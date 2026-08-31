# Calculate Body Mass Index (BMI) 
# Input weight (kg) and height (m), then calculate: 
# BMI = weight / (height ** 2)

height = float(input("Enter height: "))

weight = float(input("Enter weight: "))

bmi = weight / (height ** 2)

print(f"BMI: {bmi:.2f}")