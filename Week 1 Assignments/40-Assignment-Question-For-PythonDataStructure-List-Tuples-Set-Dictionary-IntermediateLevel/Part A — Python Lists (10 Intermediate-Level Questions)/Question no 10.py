# 10. Split a list into two lists: one with even numbers, one with odd numbers. 

numbersList = [ i for i in range(0,21) ]

print(f"List of numbers from 0-20: {numbersList}")

evenNumbersList = [ i for i in numbersList if i % 2 == 0 ]

oddNumbersList = [ i for i in numbersList if i % 2 != 0 ]

print(f"After spliiting original list to list of even numbers: {evenNumbersList}")

print(f"After spliiting original list to list of odd numbers: {oddNumbersList}")