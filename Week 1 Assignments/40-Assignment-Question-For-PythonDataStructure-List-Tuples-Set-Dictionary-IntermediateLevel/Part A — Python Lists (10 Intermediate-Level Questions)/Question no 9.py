# 9. Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]). 

numList = [1,2,3,4]

print(f"List of numbers: {numList}")

lastItem = numList.pop()

numList.insert(0,lastItem)

print(f"After rotating list: {numList}")

# Practice program

evenNumbersList = [0, 2, 4, 6, 8]

print(f"Even numbers list: {evenNumbersList}")

choice = input("Do you want to rotate the list ? (y/n): ").lower()

while choice == 'y':

    lastItem = evenNumbersList.pop()

    evenNumbersList.insert(0,lastItem)

    print(f"After rotating list: {evenNumbersList}")

    choice = input("Do you want to rotate the list ? (y/n): ").lower()

print("Program end")