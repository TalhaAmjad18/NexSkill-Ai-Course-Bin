# 6. Check if two tuples contain the same elements regardless of order.

lenOne = int(input("Enter length of tuple 1: "))

tupleOne = ()

for i in range(lenOne):

    item = input(f"Enter item {i+1} to the tuple 1: ")

    tupleOne = tupleOne + (item,)

print(f"Tuple 1: {tupleOne}")

lenTwo = int(input("Enter length of tuple 2: "))

tupleTwo = ()

for i in range(lenTwo):

    item = input(f"Enter item {i+1} to the tuple 2: ")

    tupleTwo = tupleTwo + (item,)

print(f"Tuple 2: {tupleTwo}")

if lenOne != lenTwo:

    print(f"{tupleOne} and {tupleTwo} doesnot contain same values")

else:

    d1 = {}

    for i in tupleOne:

        counterOne = 0

        j = i

        for k in tupleOne:

            if j == k:

                counterOne += 1

        d1.update({j:counterOne})

    # print(f"Tuple 1 elements occurances: {d1}")

    d2 = {}

    for i in tupleTwo:

        counterTwo = 0

        j = i

        for k in tupleTwo:

            if j == k:

                counterTwo += 1

        d2.update({j:counterTwo})

    # print(f"Tuple 2 elements occurances: {d2}")

    if d1 == d2:

        print(f"{tupleOne} and {tupleTwo} contain same values regardless of order")

    else:

        print(f"{tupleOne} and {tupleTwo} doesnot contain same values")