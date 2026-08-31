# Convert Minutes to Hours and Minutes 
# Input number of minutes and convert to hours and remaining minutes. 
# Example: 130 minutes → 2 hours 10 minutes

min = int(input("Enter minutes: "))

hours = min // 60

minutes = min - (hours * 60)

print(f"{min} minutes -> {hours} hours {minutes} minutes")