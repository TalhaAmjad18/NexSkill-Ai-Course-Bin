#  Create a program that converts minutes into hours and remaining minutes. 

minutes = int(input("Enter minutes: "))

if minutes < 60:

    print(f"{minutes} minutes => 0 hours and {minutes} minutes")

else:

    hours = minutes // 60

    remainingMinutes = minutes % (hours * 60)

    print(f"{minutes} minutes => {hours} hours and {remainingMinutes} minutes")